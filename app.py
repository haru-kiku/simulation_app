from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")  # templatesフォルダ内のindex.htmlを表示する


@app.route("/index", methods=["POST"])
def handle_data():
    chosen_image = request.form["chosen_image"]
    # ここで chosen_image を使って何か処理を行います。
    print(chosen_image)
    if chosen_image == "futa":
        photo = "futa月見坂.jpg"
    else:
        photo = "sho月見坂.jpg"
    return render_template("index_1.html", photo=photo)


@app.route("/index_2", methods=["POST"])
def select():
    chosen_preference = request.form["chosen_preference"]
    # ここで chosen_preference を使って何か処理を行います。
    print(chosen_preference)
    chosen_photo = request.form["photo"]

    # choice = input("どちらか選んでください")

    if chosen_preference == "食事":
        choice_1 = "景色がいいところで"

        choice_2 = "ちょっと一息"

        if "sho" in chosen_photo:
            photo = "sho月見坂2.jpg"
        else:
            photo = "futa中尊寺.jpg"

        return render_template("index_2.html", choice_1=choice_1, choice_2=choice_2, photo=photo)

    else:
        choice_1 = "お寺と"

        choice_2 = "風景と"

        if "sho" in chosen_photo:
            photo = "sho月見坂2.jpg"
        else:
            photo = "futa中尊寺.jpg"

        return render_template("index_2.html", choice_1=choice_1, choice_2=choice_2, photo=photo)



@app.route("/index_3", methods=["POST"])
def select2():
    chosen_preference = request.form["chosen_preference"]
    # ここで chosen_preference を使って何か処理を行います。
    print(chosen_preference)
    # choice = input("どちらか選んでください")
    if choice_1 == "食事":
        if choice_2 == "景色がいいところ":
            photo1 = "かんざん亭.jpg"
            photo2 = "義家2.jpg"
        else: 
            photo1 = "弁慶園.jpg"
            photo2 = "奥の細道展.jpg"
    else:
        if choice_2 == "お寺":
            photo1 = "金色堂.jpg"
            photo2 = "中尊寺紅葉.jpg"
        else: 
            photo1 = "月見坂.jpg"
            photo2 = "東見物台.jpg"
   
    return render_template("index_3.html", choice_1, choice_2, photo1, photo2 )


@app.route("/index_4", methods=["POST"])
def select3():
    chosen_preference = request.form["chosen_preference"]
    # ここで chosen_preference を使って何か処理を行います。
    print(chosen_preference)
    # choice = input("どちらか選んでください")
    if chosen_preference == "金鶏山":
        photo = "金鶏山１.jpg"
    else:
        photo = "無量光院跡1.jpg"
    return render_template("index_4.html", photo=photo)


@app.route("/index_5", methods=["POST"])
def select4():
    chosen_preference = request.form["chosen_preference"]
    # ここで chosen_preference を使って何か処理を行います。
    print(chosen_preference)

    # choice = input("どちらか選んでください")

    if chosen_preference == "買い物&休憩":
        choice_1 = "買い物&休憩"
        photo = "あやめ.jpg"
        return render_template("index_5.html", choice_1=choice_1, photo=photo)

    else:
        choice_1 = "体験"
        photo = "毛越寺座禅.jpg"
        return render_template("index_5.html", choice_1=choice_1, photo=photo)


if __name__ == "__main__":
    app.run()
