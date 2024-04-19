import re

def extract_sentence_between_herr_frau_and_wohnhaft(text_file_path):
    with open(text_file_path, 'r') as file:
        content = file.read()
        # Modified regex to capture text between "Herr/Frau" and "wohnhaft", and the sentence after "wohnhaft" up to the next comma
        pattern = r'(?i)(Herr|Frau)(.*?)(wohnhaft)(.*?,.*?)(?=,)'
        matches = re.findall(pattern, content)
        # Extract the second and fourth groups from each match, which are the text between "Herr/Frau" and "wohnhaft" and the sentence after "wohnhaft" up to the next comma
        results = [match[1].strip() + ' ' + match[3].strip() for match in matches]
    return results

# Example usage
text_file_path = '/home/prmahan/test/handels/doc1.txt' #Put your path 
sentences_between_herr_frau_and_wohnhaft = extract_sentence_between_herr_frau_and_wohnhaft(text_file_path)
print(type(sentences_between_herr_frau_and_wohnhaft))
print(len(sentences_between_herr_frau_and_wohnhaft))
# Print each sentence on a new line
print('\n'.join(sentences_between_herr_frau_and_wohnhaft))
