import numpy

"""
计算两个向量的余弦相似度（衡量方向相似性，剔除长度影响）

参数：
    vec_a (np.array): 向量A
    vec_b (np.array): 向量B
返回：
    float: 余弦相似度结果（范围[-1,1]，越接近1方向越一致）
公式：
    cos_sim = (vec_a · vec_b) / (||vec_a|| × ||vec_b||)
    拆解：
    1. 点积：vec_a · vec_b = vec_a[0]×vec_b[0] + vec_a[1]×vec_b[1] + ... + vec_a[n]×vec_b[n]
    2. 模长：||vec_a|| = √(vec_a[0]² + vec_a[1]² + ... + vec_a[n]²)
    3. 模长：||vec_b|| = √(vec_b[0]² + vec_b[1]² + ... + vec_b[n]²)

A: [0.5, 0.5]
B: [0.7, 0.7]
C: [0.7, 0.5]
D: [-0.6, -0.5]
"""

def get_dot(vec_a, vec_b):
    """计算2个向量的点积，2个向量同维度数字乘积之和"""
    if len(vec_a) != len(vec_b):
        raise ValueError("向量维度不一致")

    dot_sum = 0
    for a, b in zip(vec_a, vec_b):
        dot_sum += a * b

    return dot_sum

def get_norm(vec):
    """计算单个向量的模长，向量中数字的平方和开根号"""
    sum_square = 0
    for a in vec:
        sum_square += a ** 2

    # return mod_sum ** 0.5
    return numpy.sqrt(sum_square)

def consine_similarity(vec_a, vec_b):
    """计算余弦相似度"""
    dot_product = get_dot(vec_a, vec_b)
    norm_a = get_norm(vec_a)
    norm_b = get_norm(vec_b)

    return dot_product / (norm_a * norm_b)

if __name__ == "__main__":
    vec_a = [0.5, 0.5]
    vec_b = [0.7, 0.7]
    vec_c = [0.7, 0.5]
    vec_d = [-0.6, -0.5]

    print(consine_similarity(vec_a, vec_b))
    print(consine_similarity(vec_a, vec_c))
    print(consine_similarity(vec_a, vec_d))