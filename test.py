P = 2**64 - 59

flags = [
    "420d66ffc695a390bcc41c89dd521f355bf8a1ce8bc62b0180671b53d2e891a8",
    "4296c6ee787bac7de665521d490c63dc61ae9c81de6688266a0577c72448a498",
    "b0839215cb365aed8c7c033ef9e056202b3d847a5cbbd9db7ac9c8f0ad851aff",
    "6a2190aa0779831e8f3a87a922a01c3c05bc55fe94f22b99b6cf9c8b22d2a148",
    "4ddb32dbdce721e235de3062ab0c652671c08fd6a26524eb8359b2c9472971a3",
    "f314e4db3ff276736a12d4109325c66c5aab06318dce9fb8eea4ddfa36b2adb5",
    "ba7c7348d96337ca34e197eea20f768c094e604ceb34844d6e9759d3bf0de937",
    "8fe700cd09c6930261a71d3f75981625b83f3bcd5391b161e280bbbfd4078350",
    "464830fac0d902b1e193a8045a68fef6bdd8222a7e32cf7163a2912ed63eb867",
    "8d3a204ece50cdea3d35d5c16bca71d7961841a01f1071dbafd6dc5a441da049",
    "a75e2154fd95ebaefb63cb2d469d9d40062e3e32dce8c339b154f634d8f0eeb1",
    "10405faceec8e4e858c1de99d079861bebece22f18a1dfbeaf38819bc16a4891",
    "8afef7978c20be4f9e3061892df1b4cc4bb0b4ab9b9456110cfd18f1f907ebff",
    "2f5271e051f27f3fe91081d084796a47f4bb2af80b87e88f6197f7add482fe94",
    "879e8a07b5658f7995eec82d86342dcf245d013441a1b4346d03e5171f7e894a",
    "728d50e73e997cd4515a7c5568887012fc70406d739dc3cdad9cb5ad0337c462",
    "ba7c7348d96337ca34e197eea20f768c094e604ceb34844d6e9759d3bf0de937",
    "b644c1e209b41a83e9ed72be2f7878f8eb9c34fde9a06f0e9701f5448840e16a",
    "f314e4db3ff276736a12d4109325c66c5aab06318dce9fb8eea4ddfa36b2adb5",
    "b0839215cb365aed8c7c033ef9e056202b3d847a5cbbd9db7ac9c8f0ad851aff"
]

def parse_mac(mac):
    mac = mac.strip().lower()
    if len(mac) != 64:
        raise ValueError(f"MAC invalide (longueur {len(mac)} au lieu de 64): {mac}")

    x = int(mac[0:16], 16)
    a = int(mac[16:32], 16)
    b = int(mac[32:48], 16)
    c = int(mac[48:64], 16)
    return x, a, b, c

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def modinv(a, p):
    a %= p
    g, x, _ = egcd(a, p)
    if g != 1:
        raise ValueError("inverse impossible")
    return x % p

def lagrange_eval_at_zero(points, p):
    res = 0
    n = len(points)

    for i in range(n):
        xi, yi = points[i]
        num = 1
        den = 1

        for j in range(n):
            if i == j:
                continue
            xj, _ = points[j]
            num = (num * (-xj % p)) % p
            den = (den * ((xi - xj) % p)) % p

        li0 = num * modinv(den, p) % p
        res = (res + yi * li0) % p

    return res

seen = set()
pts_R, pts_S, pts_T = [], [], []

for mac in flags:
    X, A, B, C = parse_mac(mac)
    if X in seen:
        continue
    seen.add(X)
    pts_R.append((X, A))
    pts_S.append((X, B))
    pts_T.append((X, C))

print(f"Points uniques : {len(pts_R)}")

if len(pts_R) >= 9:
    R0 = lagrange_eval_at_zero(pts_R[:9], P)
    print("R(0) =", R0)
    print("hex(R(0)) =", hex(R0))
else:
    print("Pas assez de points pour R")

if len(pts_S) >= 17:
    S0 = lagrange_eval_at_zero(pts_S[:17], P)
    print("S(0) =", S0)
    print("hex(S(0)) =", hex(S0))
else:
    print("Il manque", 17 - len(pts_S), "point(s) pour S(0)")

if len(pts_T) >= 25:
    T0 = lagrange_eval_at_zero(pts_T[:25], P)
    print("T(0) =", T0)
    print("hex(T(0)) =", hex(T0))
else:
    print("Il manque", 25 - len(pts_T), "point(s) pour T(0)")