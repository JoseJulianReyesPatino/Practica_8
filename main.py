class Calculator:
    
    def sum(self, a: int, b: int) -> int:
        return a + b  # CORREGIDO
    
    def subtract(self, a: int, b: int) -> int:
        return a - b  # CORREGIDO
    
    def multiply(self, a: int, b: int) -> int:
        return a * b  # CORREGIDO
    
    def divide(self, a: int, b: int) -> float:
        if b == 0:  # CORREGIDO: manejo de división entre cero
            raise ValueError("No se puede dividir entre cero")
        return a / b