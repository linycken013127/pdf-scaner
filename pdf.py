import PyPDF2
import os

def get_all_file_list(dir):
    file_list = []
    for file in os.listdir(dir):
        if file.endswith(".pdf"):
            print(os.path.join(dir, file))
            file_list.append(os.path.join(dir, file))

    return file_list


def get_all_pdf_doc(path, print=False):
    reader = PyPDF2.PdfFileReader(path)
    text = ''
    for page in reader.pages:
        if print:
            print(page.extract_text())
        text += page.extract_text()
    return page.extract_text()

def find_text_target(text, target_start, target_end):
    return text[text.find(target_start):text.find(target_end)]

def get_file_target(path, target_start, target_end):

    file_list = get_all_file_list(path)
    # print(file_list)
    # print('='*100)

    file_number_list = []
    for file in file_list:
        text = get_all_pdf_doc(file)
        # print(os.path.basename(file)+": ", find_text_target(text, target, target2))
        file_number_list.append([os.path.basename(file), str(find_text_target(text, target_start, target_end))])

    return file_number_list

path = ''
target_start = ''
target_end = ''
print(get_file_target(path, target_start, target_end))