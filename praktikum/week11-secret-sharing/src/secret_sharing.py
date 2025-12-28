import random

# Bilangan prima besar untuk modulo
PRIME = 208351617316091241234326746312124448251235562226470491514186331217050270460481

def _eval_polynomial(coeffs, x):
    result = 0
    for i, coeff in enumerate(coeffs):
        result = (result + coeff * pow(x, i, PRIME)) % PRIME
    return result

def split_secret(secret_int, k, n):
    coeffs = [secret_int] + [random.randrange(0, PRIME) for _ in range(k - 1)]
    shares = [(i, _eval_polynomial(coeffs, i)) for i in range(1, n + 1)]
    return shares

def recover_secret(shares):
    secret = 0
    for j, (xj, yj) in enumerate(shares):
        num, den = 1, 1
        for m, (xm, _) in enumerate(shares):
            if m != j:
                num = (num * (-xm)) % PRIME
                den = (den * (xj - xm)) % PRIME
        secret = (secret + yj * num * pow(den, -1, PRIME)) % PRIME
    return secret


# ===== MAIN PROGRAM =====
if __name__ == "__main__":
    secret = "KriptografiUPB2025"
    secret_int = int.from_bytes(secret.encode(), "big")

    shares = split_secret(secret_int, 3, 5)
    print("Shares:", shares)

    recovered_int = recover_secret(shares[:3])
    recovered = recovered_int.to_bytes(
        (recovered_int.bit_length() + 7) // 8, "big"
    ).decode()

    print("Recovered secret:", recovered)
