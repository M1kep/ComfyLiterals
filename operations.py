class Operation:
    def __init__(self, ):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "A Type": (["Int", "Float"],),
                "B Type": (["Int", "Float"],),
                "Operation": (["A+B", "A-B", "A*B", "A/B"],)
            },
            "optional": {
                "A - Int": ("INT", {"forceInput": True}),
                "A - Float": ("FLOAT", {"forceInput": True}),
                "B - Int": ("INT", {"forceInput": True}),
                "B - Float": ("FLOAT", {"forceInput": True})
            }
        }

    RETURN_TYPES = ("INT", "FLOAT")
    FUNCTION = "do_operation"

    CATEGORY = "Literals"

    def _do_addition(self, a_val, b_val):
        return (int(a_val + b_val), float(a_val + b_val))

    def _do_subtraction(self, a_val, b_val):
        return (int(a_val - b_val), float(a_val - b_val))

    def _do_multiplication(self, a_val, b_val):
        return (int(a_val * b_val), float(a_val * b_val))

    def _do_division(self, a_val, b_val):
        return (int(a_val / b_val), float(a_val / b_val))

    def do_operation(self, **kwargs):
        print(f"PrintNode: {kwargs}")
        is_a_int = kwargs["A Type"] == "Int"
        is_b_int = kwargs["B Type"] == "Int"
        a_val = kwargs["A - Int"] if is_a_int else kwargs["A - Float"]
        b_val = kwargs["B - Int"] if is_b_int else kwargs["B - Float"]

        if kwargs["Operation"] == "A+B":
            return self._do_addition(a_val, b_val)
        elif kwargs["Operation"] == "A-B":
            return self._do_subtraction(a_val, b_val)
        elif kwargs["Operation"] == "A*B":
            return self._do_multiplication(a_val, b_val)
        elif kwargs["Operation"] == "A/B":
            return self._do_division(a_val, b_val)
        else:
            raise Exception("Invalid operation provided")
