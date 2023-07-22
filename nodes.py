class IntLiteral:
    def __init__(self, ):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Number": ("STRING", {}),
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "to_int"

    CATEGORY = "Literals"

    def to_int(self, Number):
        try:
            ret_val = int(Number)
        except Exception:
            raise Exception("Invalid value provided for INT")
        return (ret_val,)


class FloatLiteral:
    def __init__(self, ):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Number": ("STRING", {}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "to_float"

    CATEGORY = "Literals"

    def to_float(self, Number):
        try:
            ret_val = float(Number)
        except Exception:
            raise Exception("Invalid value provided for FLOAT")
        return (ret_val,)


class StringLiteral:
    def __init__(self, ):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "String": ("STRING", {}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "to_string"

    CATEGORY = "Literals"

    def to_string(self, String):
        return (String,)
