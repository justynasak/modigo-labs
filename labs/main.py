def find_phone_number(contacts, name):
    # TODO: build a dict from `contacts` (list of (name, phone) tuples),
    # then return the phone number for `name`, or "Not found"
    caller = {}
    for contact_name,phone_number in contacts:
        caller[contact_name] = phone_number
    return caller.get(name,"Not found")