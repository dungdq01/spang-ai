from flask_cors import CORS
from flask import Flask, jsonify, request
from human import human
from human.script import check_sinh, ngu_hanh, KIM, MOC, THUY, HOA, THO
from human.only import only_human
from human.relation import relation_config, relation_humans
# from flask import Flask, request, jsonify
from room.viet_to_trad import family_name, get_traditional_chinese,vietnamese_convert, lookup_traditional 
from head import chinese_simplify_stroke, chinese_traditional_stroke, analysis, stroke
from room.simp_to_trad.simp_to_trad import SimplifiedToTraditionalConverter
from read_json_file import read_json_file
import os
from flask_cors import cross_origin
from gift_utils import enrich_output_with_descriptions
import re
app = Flask(__name__)
CORS(app) 


data_convert_name = os.path.join(os.path.dirname(__file__), 'room', 'cabinet')

family_names_json =  os.path.join(data_convert_name, 'family_name.json')
family_names = read_json_file(family_names_json)

vn_dict_to_simp_json =  os.path.join(data_convert_name, 'vn_dict_to_simp.json')
vn_to_simp = read_json_file(vn_dict_to_simp_json)

simp_to_trad_json =  os.path.join(data_convert_name, 'simp_to_trad.json')
simp_to_trad_dict = read_json_file(simp_to_trad_json)

vn_train_json =  os.path.join(data_convert_name, 'vn_train.json')
vn_train = read_json_file(vn_train_json) 
# Initialize the converter once to be reused in requests
simp_to_trad_converter = SimplifiedToTraditionalConverter()
 
# data get stroke
data_get_stroke = os.path.join(os.path.dirname(__file__), 'head', 'cabinet')

traditional_stroke_json =  os.path.join(data_get_stroke, 'traditional_stroke.json')
traditional_stroke = read_json_file(traditional_stroke_json)

simplify_stroke_json =  os.path.join(data_get_stroke, 'simplify_stroke.json')
simplify_stroke = read_json_file(simplify_stroke_json)
# Helper Functions to encapsulate logic


@app.route('/convert', methods=['GET', 'POST'])
def convert_name():
    # Extract data based on the request method
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON payload provided"}), 400
    else:  # GET
        data = request.args

    # Retrieve parameters
    family_name_vietnamese = data.get('family_name')
    given_name_vietnamese = data.get('given_name')
    language = data.get('language')

    # Validate required parameters
    if not family_name_vietnamese or not given_name_vietnamese:
        return jsonify({"error": "Missing 'family_name' or 'given_name' parameter"}), 400

    # Set default language if not provided
    if language and isinstance(language, str):
        language = language.lower()
    else:
        language = "vietnamese"  # Fixed the assignment operator

    try:
        if language == "simplified chinese":
            # Handle Simplified Chinese to Traditional conversion
            traditional_family_name = simp_to_trad_converter.convert(family_name_vietnamese)
            traditional_given_name = simp_to_trad_converter.convert(given_name_vietnamese)

            result = {
                "traditional_family_name": traditional_family_name,
                "traditional_given_name": traditional_given_name
            }
            return jsonify(result), 200

        elif language == "vietnamese":
            # Handle Vietnamese to Traditional Chinese conversion
            traditional_family_name_converter = family_name.VietnameseFamilyNameConverter(
                family_names, family_name_vietnamese
            )
            traditional_family_name = traditional_family_name_converter.to_traditional()

            # Convert given name to traditional Chinese
            converter_name_vietnamese = vietnamese_convert.VietnameseToChineseConverter(
                given_name_vietnamese, vn_to_simp, simp_to_trad_dict
            )
            name_traditional = converter_name_vietnamese.convert_words()

            # Lookup training data
            lookup_tool = lookup_traditional.ChineseNameLookup(given_name_vietnamese, vn_train)
            name_train = lookup_tool.lookup()

            # Compare and filter results
            combine_result = get_traditional_chinese.compare_and_filter(name_traditional, name_train)
            result_given_name = combine_result.compare_and_filter_result()

            # Prepare the response
            result = {
                "traditional_family_name": traditional_family_name,
                "traditional_given_name": result_given_name
            }
            return jsonify(result), 200
        
        else:
            return jsonify({"error": f"Unsupported language: {language}"}), 400

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/stroke', methods=['POST'])
def get_stroke_count():
    data = request.get_json()
    family_name_chinese = data.get('family_name')
    given_name_chinese = data.get('given_name')
    # date_birth = data.get('date_birth')
    language = data.get('language')

    result_stroke = {}

    if language is not None:  # Hoặc isinstance(language, str)
        language = language.lower()
    if language is None:
        language = "traditional chinese"

    if not isinstance(family_name_chinese, list):
        return jsonify({"error": "Invalid input. 'characters' must be a list."})
    if not isinstance(given_name_chinese, list):
        return jsonify({"error": "Invalid input. 'characters' must be a list."})

    if language == "simplified chinese":
        result_family_name_simplify = chinese_simplify_stroke.ChineseSimplifyStrokeCounter(simplify_stroke,family_name_chinese)
        get_stroke_family_name_simplify = result_family_name_simplify.get_simplified_stroke_count()
        result_given_name_simplify = chinese_simplify_stroke.ChineseSimplifyStrokeCounter(simplify_stroke,given_name_chinese)
        get_stroke_given_name_simplify = result_given_name_simplify.get_simplified_stroke_count()
        stroke_name_list = stroke.stroke_name(get_stroke_family_name_simplify,get_stroke_given_name_simplify)
        sky_name_stroke, human_stroke, land_name_stroke = stroke_name_list.get_stroke_name()


        result_stroke["family name stroke"] = get_stroke_family_name_simplify
        result_stroke["given name stroke"] = get_stroke_given_name_simplify
        result_stroke["A"] = sky_name_stroke
        result_stroke["B"] = human_stroke
        result_stroke["C"] = land_name_stroke


    elif language == "traditional chinese":
        result_family_name_traditional = chinese_traditional_stroke.ChineseTraditionalStrokeCounter(traditional_stroke,family_name_chinese)
        get_stroke_family_name_traditional = result_family_name_traditional.get_trad_stroke_count()
        result_given_name_traditional = chinese_traditional_stroke.ChineseTraditionalStrokeCounter(traditional_stroke,given_name_chinese)
        get_stroke_given_name_traditional = result_given_name_traditional.get_trad_stroke_count()
        stroke_name_list = stroke.stroke_name(get_stroke_family_name_traditional,get_stroke_given_name_traditional)
        sky_name_stroke, human_stroke, land_name_stroke = stroke_name_list.get_stroke_name()


        result_stroke["family name stroke"] = get_stroke_family_name_traditional
        result_stroke["given name stroke"] = get_stroke_given_name_traditional
        result_stroke["A"] = sky_name_stroke
        result_stroke["B"] = human_stroke
        result_stroke["C"] = land_name_stroke
    else:
        return jsonify({"error": "Invalid language. Supported languages are 'simplified chinese' and 'traditional chinese'."})
    

    return jsonify(result_stroke) 


def get_human_info(a, b, c, date_x):
    human_obj = human.CungSo(a, b, c, date_x)
    sky, human_, land, galaxy, luunien, house, bad_year = (
        human_obj.phu_mau_cung(),
        human_obj.tat_ach_cung(),
        human_obj.tu_nu_cung(),
        human_obj.menh_cung(),
        human_obj.luu_nien(),
        human_obj.house(),
        human_obj.bad_year(),
    )
    only_human_obj = only_human.OnlyHuman(sky, human_[0], land[0], galaxy[0], date_x)
    
    menh_cach_result = only_human_obj.menh_cach()
    
    # Debug logging (commented out)
    # import sys
    # print(f"[DEBUG] menh_cach() returned: {menh_cach_result}, type: {type(menh_cach_result)}", file=sys.stderr)
    # print(f"[DEBUG] house() returned: {house}, type: {type(house)}", file=sys.stderr)
    # print(f"[DEBUG] bad_year() returned: {bad_year}, type: {type(bad_year)}", file=sys.stderr)
    
    return {
        "phu_mau": sky,
        "A4b1 ": human_[1],
        "A4b2": land[1],
        "A4b3": galaxy[1],
        "A4c1to5 ": only_human_obj.tai_khi(),
        "A4c6to9": only_human_obj.tai_kho(),
        "A4a": menh_cach_result,
        "A4d": only_human_obj.hon_nhan(),
        "A4e": luunien,
        "A4h": house,
        "A4i": bad_year,
    }

def get_relation_info(a, b, c, date_x, a1, b1, c1, date_y):
    config_relation = relation_config.PersonCreate(
        a, b, c, date_x, a1, b1, c1, date_y
    )
    info_p1, info_p2 = config_relation.create_person()
    relation_humans_ = relation_humans.RelationHuman(info_p1, info_p2)
    return {
        "A4f1f2": relation_humans_.result_khien_ban(),
        "A4f3f4": relation_humans_.check_doi_luu(),
        "A4f5f6": relation_humans_.f5_f6(),
        "A4f7f8": relation_humans_.f7_f8(),
        "A4f9f10": relation_humans_.tai_loc(),
        "A4f11f12": relation_humans_.nghiep_chuong(),
        "A4g1g2": relation_humans_.g1_2(),
        "A4g3g4": relation_humans_.g3_g4(),
        "A4g5g6": relation_humans_.khac_cot_ghi_tam(),
        "A4g7g8": relation_humans_.g7_g8_2(),
        "A4g9g10": relation_humans_.g9_g10(),
        "A4g11g12": relation_humans_.g11_g12(),
    }

def get_stroke(family_name_stroke, given_name_stroke):
    stroke_list = stroke.stroke_name(family_name_stroke, given_name_stroke)
    a,b,c = stroke_list.get_stroke_name()
    result = {"a" : a, "b" : b, "c":c}

    return result


# ===================== Transform helpers (merged from gift.py) =====================
# Mapping cho human_info (đổi nhãn sang tiếng Việt)
HUMAN_LABELS = {
    # "A4a" được phân loại riêng thành 3 nhóm ở dưới
    "A4b1 ": "Cung Mệnh",
    "A4b3": "Phân tích cung mệnh",
    "A4b2": "Sao ở cung con",
    "A4c1to5 ": "Cung tài bạch 1",  # lưu ý khoảng trắng theo nguồn
    "A4c6to9": "Cung tài bạch 2",
    "A4d": "Cung vị hôn nhân 1",
    "A4e": "Lưu niên vận",
    "A4h": "Dương trạch phong thủy",
    "A4i": "Năm đại hung",
}


def _classify_a4a(value):
    """Phân loại A4a vào 3 nhóm mệnh cách theo dải số."""
    buckets = {
        "Ngũ Hành mệnh cách 1": [],
        "Ngũ Hành mệnh cách 2": [],
        "Ngũ Hành mệnh cách 3": [],
    }

    def add_code(code):
        m = re.fullmatch(r"A4a(\d{1,2})", str(code).strip())
        if not m:
            return
        idx = int(m.group(1))
        if 1 <= idx <= 10:
            buckets["Ngũ Hành mệnh cách 1"].append(code)
        elif 11 <= idx <= 15:
            buckets["Ngũ Hành mệnh cách 2"].append(code)
        elif 16 <= idx <= 21:
            buckets["Ngũ Hành mệnh cách 3"].append(code)

    def process_value(val):
        """Recursively process nested lists/tuples"""
        if isinstance(val, str):
            add_code(val)
        elif isinstance(val, (list, tuple)):
            for item in val:
                process_value(item)
    
    process_value(value)

    # Trả chỉ các nhóm có dữ liệu
    return {k: v for k, v in buckets.items() if v}


def transform_person_output(person_dict: dict) -> dict:
    """
    Đổi nhãn sang tiếng Việt và chuẩn hóa giá trị thành danh sách mã code hoặc None.
    - A4a -> 3 khóa "Ngũ Hành mệnh cách 1/2/3" theo dải mã.
    - Các khóa còn lại map theo HUMAN_LABELS.
    - Giữ nguyên các khóa khác (ví dụ: phu_mau, "A4b1 ").
    """
    if not isinstance(person_dict, dict):
        return person_dict

    result = {}

    # Giữ nguyên các khóa không nằm trong danh sách xử lý
    for k, v in person_dict.items():
        if k not in ("A4a", "A4b1 ", "A4b2", "A4b3", "A4c1to5 ", "A4c6to9", "A4d", "A4e", "A4h", "A4i"):
            result[k] = v

    def to_list_codes(val, return_metadata=False):
        """
        Convert value to list of codes.
        If return_metadata=True and val is tuple, return dict with codes and metadata.
        """
        if val is None:
            return None
        if isinstance(val, str):
            return [val]
        if isinstance(val, tuple) and len(val) >= 2 and return_metadata:
            # Tuple với metadata: (codes, metadata)
            codes_part = val[0]
            metadata_part = val[1]
            
            # Flatten codes
            def flatten(item):
                if isinstance(item, str):
                    return [item]
                elif isinstance(item, (list, tuple)):
                    result = []
                    for sub in item:
                        result.extend(flatten(sub))
                    return result
                return []
            
            codes = flatten(codes_part)
            return {
                "codes": codes if codes else None,
                "metadata": metadata_part
            }
        elif isinstance(val, (list, tuple)):
            # Nếu là tuple nhưng không return_metadata, chỉ lấy phần codes
            if isinstance(val, tuple) and len(val) > 0:
                val = val[0]  # Lấy phần tử đầu của tuple
            
            # Flatten nested lists và lấy chỉ strings
            def flatten(item):
                if isinstance(item, str):
                    return [item]
                elif isinstance(item, (list, tuple)):
                    result = []
                    for sub in item:
                        result.extend(flatten(sub))
                    return result
                return []
            
            codes = flatten(val)
            return codes if codes else None
        return None

    # A4a -> 3 khóa tiếng Việt
    import sys
    a4a_value = person_dict.get("A4a")
    # print(f"[DEBUG transform] A4a value: {a4a_value}, type: {type(a4a_value)}", file=sys.stderr)
    
    a4a_classified = _classify_a4a(a4a_value) if "A4a" in person_dict else {}
    # print(f"[DEBUG transform] a4a_classified: {a4a_classified}", file=sys.stderr)
    
    # Luôn trả về list (có thể rỗng) hoặc None nếu không có A4a
    result["Ngũ Hành mệnh cách 1"] = to_list_codes(a4a_classified.get("Ngũ Hành mệnh cách 1")) if "A4a" in person_dict else None
    result["Ngũ Hành mệnh cách 2"] = to_list_codes(a4a_classified.get("Ngũ Hành mệnh cách 2")) if "A4a" in person_dict else None
    result["Ngũ Hành mệnh cách 3"] = to_list_codes(a4a_classified.get("Ngũ Hành mệnh cách 3")) if "A4a" in person_dict else None

    # Các khóa còn lại theo HUMAN_LABELS
    for src_key, vi_key in HUMAN_LABELS.items():
        if src_key in person_dict:
            val = person_dict.get(src_key)
            # A4h và A4i cần giữ metadata
            if src_key in ("A4h", "A4i"):
                result[vi_key] = to_list_codes(val, return_metadata=True)
            else:
                result[vi_key] = to_list_codes(val)
        else:
            result.setdefault(vi_key, None)

    return result


# Mapping cho relation_info
RELATION_F_KEYS = [
    "A4f1f2", "A4f3f4", "A4f5f6", "A4f7f8", "A4f9f10", "A4f11f12",
]
RELATION_G_KEYS = [
    "A4g1g2", "A4g3g4", "A4g5g6", "A4g7g8", "A4g9g10", "A4g11g12",
]


def _collect_codes(val) -> list:
    """Chuẩn hóa giá trị về list mã code (chuỗi)."""
    if val is None:
        return []
    if isinstance(val, str):
        return [val]
    if isinstance(val, list):
        return [x for x in val if isinstance(x, str)]
    return []


def transform_relation_output(relation_dict: dict) -> dict:
    """
    Trả 2 nhóm:
    - "Mối quan hệ công sở": danh sách các mã từ tất cả khóa A4f*.
    - "Mối quan hệ tình yêu": danh sách các mã từ tất cả khóa A4g*.
    Nếu nhóm rỗng → None.
    """
    if not isinstance(relation_dict, dict):
        return relation_dict

    cong_so_list = []
    tinh_yeu_list = []

    for k in RELATION_F_KEYS:
        cong_so_list.extend(_collect_codes(relation_dict.get(k)))

    for k in RELATION_G_KEYS:
        tinh_yeu_list.extend(_collect_codes(relation_dict.get(k)))

    return {
        "Mối quan hệ công sở": cong_so_list or None,
        "Mối quan hệ tình yêu": tinh_yeu_list or None,
    }
# API Endpoints
@app.route('/human_info', methods=['POST'])
def human_info():
    import sys
    data = request.get_json()
    family_name_chinese = data.get('family_name')
    given_name_chinese = data.get('given_name')
    human_family_name_trad = chinese_traditional_stroke.ChineseTraditionalStrokeCounter(traditional_stroke, family_name_chinese)
    human_family_name_trad_stroke = human_family_name_trad.get_trad_stroke_count()
    human_given_name_trad = chinese_traditional_stroke.ChineseTraditionalStrokeCounter(traditional_stroke, given_name_chinese)
    human_given_name_trad_stroke = human_given_name_trad.get_trad_stroke_count()
    birth = data["birth"]
    create_ = get_stroke(human_family_name_trad_stroke, human_given_name_trad_stroke)
    a, b, c = create_["a"], create_["b"], create_["c"]
    result = get_human_info(a, b, c, birth)
    # print(f"[DEBUG] get_human_info result: {result}", file=sys.stderr)
    
    transformed = transform_person_output(result)
    # print(f"[DEBUG] transformed result keys with None: {[k for k, v in transformed.items() if v is None]}", file=sys.stderr)
    
    enriched = enrich_output_with_descriptions(transformed)
    return jsonify(enriched)


@app.route('/relation_info', methods=['POST'])
def relation_info():
    data = request.get_json()
    family_name_chinese = data.get('family_name')
    given_name_chinese = data.get('given_name')
    family_name_chinese_1 = data.get('family_name_relation')
    given_name_chinese_1 = data.get('given_name_relation')
    date_x = data["birth"]
    date_y = data["birth_relation"]
    result_stroke = {}

    result_family_name_traditional = chinese_traditional_stroke.ChineseTraditionalStrokeCounter(traditional_stroke,family_name_chinese)
    get_stroke_family_name_traditional = result_family_name_traditional.get_trad_stroke_count()
    result_given_name_traditional = chinese_traditional_stroke.ChineseTraditionalStrokeCounter(traditional_stroke,given_name_chinese)
    get_stroke_given_name_traditional = result_given_name_traditional.get_trad_stroke_count()
    stroke_name_list = stroke.stroke_name(get_stroke_family_name_traditional,get_stroke_given_name_traditional)
    sky_name_stroke, human_stroke, land_name_stroke = stroke_name_list.get_stroke_name()


    result_stroke["family name stroke"] = get_stroke_family_name_traditional
    result_stroke["given name stroke"] = get_stroke_given_name_traditional
    result_stroke["A"] = sky_name_stroke
    result_stroke["B"] = human_stroke
    result_stroke["C"] = land_name_stroke
    # data = request.get_json()
    # family_name_stroke = data["family_name"]
    # given_name_stroke = data["given_name"]
    date_x = data["birth"]
    date_y = data["birth_relation"]

    # create = get_stroke(family_name_stroke, given_name_stroke)
    a,b,c =result_stroke["A"],result_stroke["B"],result_stroke["C"]


    result_stroke_1 = {}

    result_family_name_traditional_1 = chinese_traditional_stroke.ChineseTraditionalStrokeCounter(traditional_stroke,family_name_chinese_1)
    get_stroke_family_name_traditional_1 = result_family_name_traditional_1.get_trad_stroke_count()
    result_given_name_traditional_1 = chinese_traditional_stroke.ChineseTraditionalStrokeCounter(traditional_stroke,given_name_chinese_1)
    get_stroke_given_name_traditional_1 = result_given_name_traditional_1.get_trad_stroke_count()
    stroke_name_list_1 = stroke.stroke_name(get_stroke_family_name_traditional_1,get_stroke_given_name_traditional_1)
    sky_name_stroke_1, human_stroke_1, land_name_stroke_1 = stroke_name_list_1.get_stroke_name()

    result_stroke_1["family name stroke"] = get_stroke_family_name_traditional_1
    result_stroke_1["given name stroke"] = get_stroke_given_name_traditional_1
    result_stroke_1["A"] = sky_name_stroke_1
    result_stroke_1["B"] = human_stroke_1
    result_stroke_1["C"] = land_name_stroke_1 
    # print(result_stroke)
    # print(result_stroke_1)


    a1, b1, c1 = result_stroke_1["A"], result_stroke_1["B"], result_stroke_1["C"]

    relation_only = get_relation_info(a, b, c, date_x, a1, b1, c1, date_y)
    transformed_relation = transform_relation_output(relation_only)
    enriched_relation = enrich_output_with_descriptions(transformed_relation)
    return jsonify(enriched_relation)

@app.route('/get_results', methods=['POST'])
def get_descriptions():
    """
    Nhận input là dict output của endpoint logic (code hoặc list code), trả về dict đã enrich mô tả (toàn bộ JSON mapping cho mỗi code).
    Body mẫu:
    {
      "person_1": {...},
      "person_2": {...},
      "relation": {...}
    }
    """
    data = request.get_json()
    result = {}
    for key, value in data.items():
        result[key] = enrich_output_with_descriptions(value)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
