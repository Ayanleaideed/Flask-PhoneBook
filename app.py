from flask import Flask, render_template, request, redirect, url_for

# import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_entry():
    if request.method == "POST":
        if "add_btn" in request.form:
            name = request.form.get("name")
            phone = request.form.get("phone")
            if name and phone is not None:
                write_file(name, phone)
                return redirect(url_for("index"))
            return render_template("add_entry.html")
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def Search_entry():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        if name and phone:
            return "Please search by either name or phone number, not both."
        data = read_file(name, phone)
        if data:
            table_rows = []
            for entry in data:
                table_rows.append({"name": entry["Name"], "phone": entry["Phone"]})
            return render_template("results.html", rows=table_rows)
        else:
            return "No entries found."
    return render_template("search.html")


@app.route("/delete", methods=["GET", "POST"])
def Delete_entry():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")

        if name and phone:
            # Read the contents of the file
            with open("phone_book.txt", "r") as f:
                lines = f.readlines()

            # Find and remove the line(s) to delete
            new_lines = []
            for line in lines:
                if f"{name}," not in line or f"{phone}" not in line:
                    new_lines.append(line)

            # Write the updated file back
            with open("phone_book.txt", "w") as f:
                f.writelines(new_lines)
                return redirect(url_for("index"))

    return render_template("delete_entry.html")


@app.route("/edit", methods=["GET", "POST"])
def Edit_entry():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        new_name = request.form.get("new_name")
        new_number = request.form.get("new_phone")

        # Check if name and phone are not None or empty strings
        if (
            name is not None
            and phone is not None
            and name.strip() != ""
            and phone.strip() != ""
        ):
            # Read the contents of the file
            with open("phone_book.txt", "r") as f:
                lines = f.readlines()

            # Find and update the line(s)
            updated_lines = []
            found = False
            for line in lines:
                if name in line and phone in line:
                    updated_lines.append(f"{new_name},{new_number}\n")
                    found = True
                else:
                    updated_lines.append(line)

            # If no entry was found for editing, return a message
            if not found:
                return "<h1>The entry was not found</h1>"

            # Write the updated file back
            with open("phone_book.txt", "w") as f:
                f.writelines(updated_lines)

            return redirect(url_for("Search_entry"))
        else:
            return render_template("Edit.html")
            # return "<h1>Invalid input for name and phone</h1>"

    return render_template("Edit.html")


def write_file(name, phone):
    with open("phone_book.txt", "a+") as file:
        file.write(f"{str(name)},{(phone)}\n")


def read_file(name=None, phone=None):
    entries = []
    with open("phone_book.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 2:
                n, num = parts[0], parts[1]
                if name and name.lower() not in n.lower():
                    continue
                if phone and phone != num.replace("-", ""):
                    continue
                entries.append({"Name": n, "Phone": num})
    return entries


if __name__ == "__main__":
    app.run(debug=True)
