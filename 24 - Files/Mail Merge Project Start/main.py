# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# open dummy letter
with open("Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

# opening name list
with open("Input/Names/invited_names.txt") as file:
    invited_names = file.read().split()

# create personal letters
for name in invited_names:
    with open(f"Output/ReadyToSend/{name}", mode="w") as file:
        personal_letter = starting_letter.replace("[name]", f"{name}")
        file.write(personal_letter)