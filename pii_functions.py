import re

def mask_sensitive_info(text):
    # Regular expression patterns
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
    cc_pattern = r'\b(?:\d[ -]*?){13,16}\b'
    
    # Function to mask email addresses
    def mask_email(match):
        email = match.group()
        parts = email.split('@')
        masked_email = parts[0][0] + '*' * (len(parts[0]) - 2) + parts[0][-1] + '@' + parts[1]
        return masked_email
    
    # Function to mask SSNs
    def mask_ssn(match):
        ssn = match.group()
        return '***-**-' + ssn[-4:]
    
    # Function to mask credit card numbers
    def mask_cc(match):
        card_number = match.group()
        digits = re.sub(r'\D', '', card_number)
        masked = '*' * (len(digits) - 4) + digits[-4:]
        masked_card_number = ''
        digit_index = 0
        for char in card_number:
            if char.isdigit():
                masked_card_number += masked[digit_index]
                digit_index += 1
            else:
                masked_card_number += char
        return masked_card_number
    
    # Mask email addresses
    text = re.sub(email_pattern, mask_email, text)
    # Mask SSNs
    text = re.sub(ssn_pattern, mask_ssn, text)
    # Mask credit card numbers
    text = re.sub(cc_pattern, mask_cc, text)
    
    return text

# Example usage
#text = "Here are some sensitive info: email@example.com, 123-45-6789, 4111 1111 1111 1111."
#print(mask_sensitive_info(text))