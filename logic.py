from KCollections.data_collection import TEXTS, SIMBOLS

def encryption_logic(key_input):
    """ Algoritmo puro de descifrado """
    raw = key_input.replace("Key-", "").strip()
    if len(raw) < 14: return None
    try:
        idx_s1, idx_s2, idx_s3 = int(raw[1]), int(raw[3]), int(raw[6])
        num1, num2 = raw[8:10], raw[10]
        # El formato TEXT1 son los dígitos 11, 12, 13
        idx_text = int(raw[11:14]) - 100
        return TEXTS[idx_text] + SIMBOLS[idx_s1] + num2 + SIMBOLS[idx_s2] + num1 + SIMBOLS[idx_s3]
    except Exception:
        return None