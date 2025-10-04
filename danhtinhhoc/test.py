from flask import Flask, jsonify, request
from human import human
from human.script import check_sinh, ngu_hanh, KIM, MOC, THUY, HOA, THO
from human.only import only_human
from human.relation import relation_config, relation_humans
from head import stroke
# from flask import Flask, request, jsonify
from room.viet_to_trad import family_name, get_traditional_chinese,vietnamese_convert, lookup_traditional 
from head import chinese_simplify_stroke, chinese_traditional_stroke, analysis, stroke
from read_json_file import read_json_file
import os
app = Flask(__name__)

data_convert_name = os.path.join(os.path.dirname(__file__), 'room', 'cabinet')

family_names_json =  os.path.join(data_convert_name, 'family_name.json')
family_names = read_json_file(family_names_json)

vn_dict_to_simp_json =  os.path.join(data_convert_name, 'vn_dict_to_simp.json')
vn_to_simp = read_json_file(vn_dict_to_simp_json)

simp_to_trad_json =  os.path.join(data_convert_name, 'simp_to_trad.json')
simp_to_trad_dict = read_json_file(simp_to_trad_json)

vn_train_json =  os.path.join(data_convert_name, 'vn_train.json')
vn_train = read_json_file(vn_train_json) 

# data get stroke
data_get_stroke = os.path.join(os.path.dirname(__file__), 'head', 'cabinet')

traditional_stroke_json =  os.path.join(data_get_stroke, 'traditional_stroke.json')
traditional_stroke = read_json_file(traditional_stroke_json)

simplify_stroke_json =  os.path.join(data_get_stroke, 'simplify_stroke.json')
simplify_stroke = read_json_file(simplify_stroke_json)
# Helper Functions to encapsulate logic


@app.route('/convert', methods=['POST'])
def convert_name():

    # get data request
    data = request.get_json()
    family_name_vietnamese = data.get('family_name')
    given_name_vietnamese = data.get('given_name')
    language = data.get('language')

    if language is not None:  # Hoặc isinstance(language, str)
        language = language.lower()
    else:
        language == "vietnamese"

  
    traditional_family_name_converter = family_name.VietnameseFamilyNameConverter(family_names,family_name_vietnamese)
    traditional_family_name = traditional_family_name_converter.to_traditional()

    converter_name_vietnamese = vietnamese_convert.VietnameseToChineseConverter(given_name_vietnamese,vn_to_simp,simp_to_trad_dict)
    name_traditional = converter_name_vietnamese.convert_words()

    lookup_tool = lookup_traditional.ChineseNameLookup(given_name_vietnamese,vn_train)
    name_train = lookup_tool.lookup()

    combine_result = get_traditional_chinese.compare_and_filter(name_traditional, name_train)
    result_given_name  = combine_result.compare_and_filter_result()


    result = {
        "traditional_family_name": traditional_family_name,
        "traditional_given_name": result_given_name
    }

    
    return jsonify(result)


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
    return {
        "phu_mau": sky,
        "star of mind ": human_[1],
        "star of children": land[1],
        "star of life": galaxy[1],
        "money flow ": only_human_obj.tai_khi(),
        "money stock": only_human_obj.tai_kho(),
        "five elements": only_human_obj.menh_cach(),
        "marriage": only_human_obj.hon_nhan(),
        "year flow ": luunien,
        "lucky house": house,
        "bad year": bad_year,
    }

def get_relation_info(a, b, c, date_x, a1, b1, c1, date_y):
    config_relation = relation_config.PersonCreate(
        a, b, c, date_x, a1, b1, c1, date_y
    )
    info_p1, info_p2 = config_relation.create_person()
    relation_humans_ = relation_humans.RelationHuman(info_p1, info_p2)
    return {
        "heart": relation_humans_.result_khien_ban(),
        "communicate": relation_humans_.check_doi_luu(),
        "brain": relation_humans_.f5_f6(),
        "hand": relation_humans_.f7_f8(),
        "money work": relation_humans_.tai_loc(),
        "company": relation_humans_.nghiep_chuong(),
        "love relation": relation_humans_.g1_2(),
        "siging relation": relation_humans_.g3_g4(),
        "deep realation check": relation_humans_.khac_cot_ghi_tam(),
        "deep realation": relation_humans_.g7_g8_2(),
        "right relation": relation_humans_.g9_g10(),
        "sex relation": relation_humans_.g11_g12(),
    }
def get_stroke(family_name_stroke, given_name_stroke):
    stroke_list = stroke.stroke_name(family_name_stroke, given_name_stroke)
    a,b,c = stroke_list.get_stroke_name()
    result = {"a" : a, "b" : b, "c":c}

    return result


# API Endpoints
@app.route('/human_info', methods=['POST'])
def human_info():

    data = request.get_json()
    family_name_chinese = data.get('family_name')
    given_name_chinese = data.get('given_name')
    human_family_name_trad = chinese_traditional_stroke.ChineseTraditionalStrokeCounter(traditional_stroke,family_name_chinese)
    human_family_name_trad_stroke = human_family_name_trad.get_trad_stroke_count()
    human_given_name_trad = chinese_traditional_stroke.ChineseTraditionalStrokeCounter(traditional_stroke,given_name_chinese)
    human_given_name_trad_stroke = human_given_name_trad.get_trad_stroke_count()
    birth = data["birth"]
    create_ = get_stroke(human_family_name_trad_stroke, human_given_name_trad_stroke)
    
    a,b,c =create_["a"], create_["b"],create_["c"]
    result = get_human_info(a, b, c,birth)
    return jsonify(result)


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


    a1, b1, c1 = result_stroke_1["A"],result_stroke_1["B"],result_stroke_1["C"]

    result_1 = get_human_info(a, b, c,date_x)
    result_2 = get_human_info(a1, b1, c1,date_y)
    result_3 = get_relation_info(a, b, c,date_x, a1, b1, c1,date_y)
    result = {"person_1" : result_1, "person_2" : result_2,"relation" : result_3}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
