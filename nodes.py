import folder_paths

# Hack: string type that is always equal in not equal comparisons
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False


# Our any instance wants to be a wildcard string
ANY = AnyType("*")
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
                "String": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "to_string"

    CATEGORY = "Literals"

    def to_string(self, String):
        return (String,)


class CheckpointListLiteral:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "literal": ("STRING", {
                    "multiline": True,
                    "default": "\n".join(folder_paths.get_filename_list("checkpoints"))
                }),
            },
        }

    RETURN_TYPES = (ANY,)
    RETURN_NAMES = ("Selected Checkpoints",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "parse_literal"

    # OUTPUT_NODE = False

    CATEGORY = "List Stuff"

    def parse_literal(self, literal):
        split = list(filter(None, literal.split("\n")))
        return (split,)

class LoraListLiteral:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "literal": ("STRING", {
                    "multiline": True,
                    "default": "\n".join(folder_paths.get_filename_list("loras"))
                }),
            },
        }

    RETURN_TYPES = (ANY,)
    RETURN_NAMES = ("Selected Loras",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "parse_literal"

    # OUTPUT_NODE = False

    CATEGORY = "List Stuff"

    def parse_literal(self, literal):
        split = list(filter(None, literal.split("\n")))
        return (split,)
