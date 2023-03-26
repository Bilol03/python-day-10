# Function with outputs

#  Formatting name Exercise

def format_name(f_name, l_name):
  """Format the give Words """
  if f_name == "" and l_name == "":
    return "You wrote wrong name!"
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()

  return f"{formatted_f_name} {formatted_l_name}"

res = format_name(input("Please enter your first name: "),
                  input("Please enter your last name: "))
print(res)
