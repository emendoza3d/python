class Ring:
    def __init__(self, shape, style, metal, diamond):
        # Private attributes protect the order details
        self.__shape = shape
        self.__style = style
        self.__metal = metal
        self.__diamond = diamond
        

    # --- Getters ---
    def get_shape(self):
        return self.__shape

    def get_style(self):
        return self.__style

    def get_metal(self):
            return self.__metal
    
    def get_diamond(self):
            return self.__diamond

    # --- Setters ---
    def set_shape(self, shape):
        # Setters allow us to validate data before changing it
        if shape >= 0:
            self.__shape = shape

    def set_style(self, style):
                    # Setters allow us to validate data before changing it
        if style >= 0:
            self.__style = style

    def set_metal(self, metal):
            # Setters allow us to validate data before changing it
            if metal >= 0:
                self.__metal = metal

    def set_diamond(self, diamond):
            # Setters allow us to validate data before changing it
            if diamond >= 0:
                self.__diamond = diamond

    # --- Summary Output ---
    def get_summary(self):
        return (f"Order Summary: {self.__shape} shape,"
                f"with {self.__style} style, {self.__metal} metal, "
                f"and {self.__diamond} diamond.")

# Using the objects
ring1 = Ring("round", "solitaire", "gold", "natural")
ring2 = Ring("cushion", "halo", "white gold", "lab")

print(ring1.get_summary())
print(ring2.get_summary())