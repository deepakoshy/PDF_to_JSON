from pdfminer.high_level import extract_text
import json


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


if __name__ == '__main__':
    data_dict = {}
    json_path = 'Sample_Data.json'
    data = extract_text_from_pdf('Interview_sample_data[374].pdf')

    data_list = list(data.split("\n"))

    for data in data_list:
        if '__' in data:
            data_list.remove(data)

    data_list = list(filter(str.strip, data_list))

    data_list = [x.strip(' ') for x in data_list]

    # print(data_list)
    data_dict['name'] = data_list[0].strip()
    data_dict['address'] = data_list[2].strip()
    data_dict['email'] = data_list[1].split("|")[1].strip()

    subheadings = ['Education', 'Leadership Experience', 'Professional Experience', 'Additional Projects', 'Skills & Interests']
    sub_index = []


    for sub in subheadings:
        for index, word in enumerate(data_list):
            if sub in word:
                sub_index.append(index)

    for index in range(len(sub_index)):
        low = sub_index[index]+1
        if index != len(sub_index)-1:
            high = sub_index[index+1]
        else:
            high = -1

        # print(subheadings[index])
        # print("".join(data_list[low:high]))

        data_dict[subheadings[index]] = "".join(data_list[low:high])

    print(data_dict)

    with open(json_path, 'w') as fh:
        json.dump(data_dict, fh, indent = 4)


