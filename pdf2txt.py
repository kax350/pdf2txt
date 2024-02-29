import fitz  # 导入PyMuPDF库

def pdf_to_text(pdf_path, text_path):
    """
    将PDF文件转换为文字文件。

    参数:
    pdf_path: 输入的PDF文件路径。
    text_path: 输出的TXT文件路径。
    """
    # 打开PDF文件
    doc = fitz.open(pdf_path)
    
    # 创建并打开用于写入的文本文件
    with open(text_path, 'w', encoding='utf-8') as text_file:
        # 逐页读取PDF
        for page_num in range(len(doc)):
            # 获取当前页的文本
            page_text = doc.load_page(page_num).get_text("text")
            # 将文本写入文件
            text_file.write(page_text)
    
    # 关闭PDF文档
    doc.close()

# 示例用法
pdf_file_path = 'path/to/your/input.pdf'  # 输入PDF的路径
text_file_path = 'path/to/your/output.txt'  # 输出文本文件的保存路径
pdf_to_text(pdf_file_path, text_file_path)  # 调用函数进行转换
