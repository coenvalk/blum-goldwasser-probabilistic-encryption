import numpy as np


def BGW_enc(p, q, a, b, x, m):
    n = p * q

    assert a*p + b*q == 1
    # assert p%4 == 3 and q%4 == 4

    k = int(np.log2(n))
    h = int(np.log2(k))

    t = len(m) / h

    xi = x
    c = ''
    for i in range(t):
        mi = m[i*h:(i + 1)*h]
        xi = (xi ** 2) % n
        xi_bin = bin(xi)
        pi = xi_bin[-h:]

        mi_int = int(mi, 2)
        pi_int = int(pi, 2)

        ci = pi_int ^ mi_int
        ci_bin = format(ci, '0' + str(h) + 'b')
        c += ci_bin

    xt = (xi ** 2) % n
    return c, xt
        
    

def BGW_dec(p, q, a, b, xt, c):
    n = p * q
    
    k = int(np.log2(n))
    h = int(np.log2(k))

    t = len(c) / h
    
    d1 = (((p + 1) / 4)**(t + 1)) % (p - 1)
    d2 = (((q + 1) / 4)**(t + 1)) % (q - 1)

    u = (xt**d1) % p
    v = (xt**d2) % q

    x0 = (v*a*p + u*b*q) % n

    xi = x0
    m = ''
    for i in range(t):
        ci = c[i*h:(i + 1)*h]
        xi = (xi**2) % n
        xi_bin = bin(xi)
        pi = xi_bin[-h:]
        ci_int = int(ci, 2)
        pi_int = int(pi, 2)

        mi = pi_int ^ ci_int
        mi_bin = format(mi, '0' + str(h) + 'b')
        m += mi_bin

    return m



if __name__ == "__main__":
    m = '10011100000100001100'
    
    p = 499
    q = 547
    a = -57
    b = 52
    x0 = 159201
    
    
    c, xt = BGW_enc(p, q, a, b, x0, m)
    print "ciphertext:", c
    d = BGW_dec(p, q, a, b, xt, c)
    
    print "asserting that decrypted plaintext == m..."
    assert m == d
    print "assertion correct! done."
