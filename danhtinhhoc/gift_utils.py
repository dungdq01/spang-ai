import json
import os
import sys
from typing import Optional, Dict, Any

def load_json_mapping(code: str) -> Optional[Dict[str, Any]]:
    """
    Trả về toàn bộ dict JSON mapping cho 1 code cụ thể.
    """
    if not isinstance(code, str):
        return None
    
    # Ưu tiên lấy folder 4 ký tự đầu (A4b1, A4b2...), nếu không có thì fallback về 3 ký tự
    # Xử lý code có khoảng trắng: "A4b1 No.16" -> lấy "A4b1"
    code_prefix = code.split()[0] if ' ' in code else code[:4]
    # Folder names are like: A4b1, A4b2, A4c, A4d (NOT uppercase)
    group4 = code_prefix[:4]  # Keep original case: A4b1
    group3 = code_prefix[:3]  # Keep original case: A4c
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folder4 = os.path.join(base_dir, 'data', group4)
    folder3 = os.path.join(base_dir, 'data', group3)
    
    # Debug logging (commented out for production)
    # print(f"[DEBUG] Looking for code: {code}", file=sys.stderr)
    # print(f"[DEBUG] Base dir: {base_dir}", file=sys.stderr)
    # print(f"[DEBUG] Trying folder4: {folder4}, exists: {os.path.isdir(folder4)}", file=sys.stderr)
    # print(f"[DEBUG] Trying folder3: {folder3}, exists: {os.path.isdir(folder3)}", file=sys.stderr)
    
    if os.path.isdir(folder4):
        folder = folder4
    elif os.path.isdir(folder3):
        folder = folder3
    else:
        # print(f"[DEBUG] No folder found for code: {code}", file=sys.stderr)
        return None
    
    print(f"[DEBUG] Using folder: {folder}", file=sys.stderr)
    
    # Tìm file json chứa code này
    # Thử tìm file chính xác trước
    exact_filename = f"{code}.json"
    exact_path = os.path.join(folder, exact_filename)
    
    # print(f"[DEBUG] Looking for exact file: {exact_path}", file=sys.stderr)
    
    if os.path.isfile(exact_path):
        try:
            # print(f"[DEBUG] Found exact file: {exact_path}", file=sys.stderr)
            with open(exact_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            # print(f"[ERROR] Error loading {exact_path}: {e}", file=sys.stderr)
            return None
    
    # Nếu không tìm thấy, thử tìm file bắt đầu với code (case-insensitive)
    # print(f"[DEBUG] Exact file not found, searching in folder...", file=sys.stderr)
    try:
        files = os.listdir(folder)
        # print(f"[DEBUG] Files in folder: {files[:5]}...", file=sys.stderr)
        
        for fname in files:
            if fname.lower().startswith(code.lower()) and fname.endswith('.json'):
                fpath = os.path.join(folder, fname)
                # print(f"[DEBUG] Found matching file: {fpath}", file=sys.stderr)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        return json.load(f)
                except Exception as e:
                    # print(f"[ERROR] Error loading {fpath}: {e}", file=sys.stderr)
                    continue
    except Exception as e:
        return None
    #     print(f"[ERROR] Error listing folder {folder}: {e}", file=sys.stderr)
    
    # print(f"[DEBUG] No matching file found for code: {code}", file=sys.stderr)
    return None

def get_code_description(code: str) -> dict:
    """
    Trả về toàn bộ dict JSON mapping cho 1 code (mọi ngôn ngữ, mọi trường)
    """
    if not isinstance(code, str):
        return {}
    content_dict = load_json_mapping(code)
    if content_dict:
        return content_dict
    return {}

def enrich_output_with_descriptions(output):
    """
    Nhận đầu vào là dict, list, string hoặc số, trả về object đã enrich mô tả code ở mọi cấp.
    Xử lý đặc biệt cho dict có keys "codes" và "metadata" (A4h, A4i).
    """
    if isinstance(output, dict):
        # Kiểm tra nếu là dict với "codes" và "metadata" (từ A4h, A4i)
        if "codes" in output and "metadata" in output:
            codes_list = output["codes"]
            metadata = output["metadata"]
            
            # Enrich codes
            enriched_codes = None
            if codes_list:
                enriched_codes = [
                    {"code": code, "description": get_code_description(code)}
                    for code in codes_list
                ]
            
            return {
                "codes": enriched_codes,
                "metadata": metadata  # Giữ nguyên metadata
            }
        else:
            # Dict thông thường, recurse vào từng value
            return {k: enrich_output_with_descriptions(v) for k, v in output.items()}
    elif isinstance(output, list):
        return [enrich_output_with_descriptions(item) for item in output]
    elif isinstance(output, str):
        return {"code": output, "description": get_code_description(output)}
    else:
        return output
