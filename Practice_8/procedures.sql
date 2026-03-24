CREATE OR REPLACE PROCEDURE delete_contact_by_name_or_phone(p_val VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE user_name = p_val OR phone_number = p_val;
END;
$$;
