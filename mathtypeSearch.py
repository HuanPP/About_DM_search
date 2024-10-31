import tkinter as tk
from tkinter import messagebox

mathtype_dict = {
    "集合运算": [
        ("\\cup", "∪"), ("\\cap", "∩"), ("\\setminus", "∖"),
        ("\\subset", "⊂"), ("\\subseteq", "⊆"), ("\\supset", "⊃"), ("\\supseteq", "⊇"),
        ("\\in", "∈"), ("\\notin", "∉"), ("\\emptyset", "∅"), ("\\bigcup", "⋃"),
        ("\\bigcap", "⋂"), ("\\complement", "补集符号"),
        ("\\mathbb{P}(A)", "幂集")
    ],
    "逻辑运算": [
        ("\\wedge", "∧"), ("\\vee", "∨"), ("\\neg", "¬"),
        ("\\Rightarrow", "⇒"), ("\\Leftrightarrow", "⇔"), ("\\forall", "∀"), ("\\exists", "∃"),
        ("\\nexists", "不存在 ∄"), ("\\top", "真值 ⊤"), ("\\bot", "假值 ⊥")
    ],
    "关系运算": [
        ("=", "="), (">", ">"), ("<", "<"), ("\\geq", "≥"), ("\\leq", "≤"),
        ("\\neq", "≠"), ("\\equiv", "≡"), ("\\cong", "≅"),
        ("\\sim", "相似 ∼"), ("\\asymp", "渐近 ≍"), ("\\propto", "成比例 ∝")
    ],
    "组合数学": [
        ("\\binom{n}{k}", "组合符号 C(n, k)"), ("\\sum", "∑"), ("\\prod", "∏"),
        ("\\frac{n!}{(n-k)!}", "排列符号 P(n, k)"), ("\\lfloor x \\rfloor", "向下取整 ⌊x⌋"),
        ("\\lceil x \\rceil", "向上取整 ⌈x⌉"), ("\\binom{n+k-1}{k}", "重复组合")
    ],
    "数论": [
        ("\\bmod", "mod运算符"), ("\\gcd", "gcd 最大公约数"), ("\\text{lcm}", "lcm 最小公倍数"),
        ("\\mathbb{Z}", "整数集合 Z"), ("\\mathbb{N}", "自然数集合 N"),
        ("\\mathbb{Q}", "有理数集合 Q"), ("\\mathbb{R}", "实数集合 R"),
        ("\\mathbb{C}", "复数集合 C"), ("\\varphi(n)", "欧拉函数 φ(n)"),
        ("\\pi(n)", "质数计数函数 π(n)"), ("\\mid", "整除符号 |"),
        ("\\nmid", "不整除符号 ∤")
    ],
    "函数与映射": [
        ("f: A \\to B", "从集合A到集合B的函数"), ("f: A \\to B \\mid f(a) = b", "带映射定义的函数"),
        ("\\circ", "复合函数符号"), ("\\leftarrow", "逆映射"), ("f^{-1}(x)", "逆函数"),
        ("f \\in C(X)", "连续函数"), ("f \\in L^2(X)", "二次可积函数"), ("f(x) = O(g(x))", "渐进上界符号 O"),
        ("f(x) = \\Theta(g(x))", "渐进等价 Θ")
    ],
    "其他常用符号": [
        ("\\infty", "∞"), ("\\sqrt", "√"), ("\\parallel", "平行 ||"),
        ("\\perp", "垂直 ⊥"), ("\\angle", "角度 ∠"), ("\\triangle", "三角形 △"),
        ("\\sum", "∑"), ("\\prod", "∏"), ("\\nabla", "∇ 微分算符"),
        ("\\partial", "偏导数 ∂"), ("\\therefore", "所以 ∴"), ("\\because", "因为 ∵"),
        ("\\vdots", "纵向省略号 ⋮"), ("\\ddots", "对角省略号 ⋱"), ("\\cdots", "横向省略号 ⋯")
    ]
}

# 搜索符号函数
def search_mathtype():
    query = selected_option.get()
    results = mathtype_dict.get(query, [])
    if results:
        result_text = f"与 '{query}' 相关的 MathType 符号代码:\n\n"
        for code, symbol in results:
            result_text += f"{symbol} : {code}\n"
        result_label.config(text=result_text)
    else:
        result_label.config(text=f"未找到与 '{query}' 相关的 MathType 符号。")

# 创建主窗口
root = tk.Tk()
root.title("离散数学符号查找工具")
root.geometry("400x400")

# 使用说明标签
usage_label = tk.Label(root, text="请选择关键词（如'集合运算'、'逻辑运算'等）:")
usage_label.pack(pady=5)

# 下拉菜单选项
options = list(mathtype_dict.keys())
selected_option = tk.StringVar(root)
selected_option.set(options[0])  # 设置默认值

# 下拉菜单
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.pack(pady=5)

# 搜索按钮
search_button = tk.Button(root, text="搜索", command=search_mathtype)
search_button.pack(pady=5)

# 结果显示区域
result_label = tk.Label(root, text="", justify="left", anchor="w")
result_label.pack(pady=5, padx=10)

# 主循环
root.mainloop()