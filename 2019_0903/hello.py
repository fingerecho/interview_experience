
def func(L) -> int:
    m = float('-inf')
    for i in range(0,len(L)-1):
        for j in range(i,len(L)):
            if m < L[j] - L[i]:
                m = L[j] - L[i]
    return m

def func_0(L) -> int:
    if len(L) == 0: return None
    m = float('-inf')
    m_l = L[0]
    m_r = L[1]
    m = m_r - m_l
    for i in range(2,len(L)):
        if m_l > L[i]:
            m_l = L[i]
        if m_r < L[i]:
            m_r = L[i]
        if m_r - m_l > m:
            m = m_r - m_l
    return m


    
