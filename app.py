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
    if chosen_image == "chosen_image":
        photo = "f_tukimi.jpg"
    else:
        photo = "s_tukimi.jpg"
    return render_template("index_1.html", photo=photo)


@app.route("/index_2", methods=["POST"])
def select():
    chosen_preference = request.form["chosen_preference"]
    # ここで chosen_preference を使って何か処理を行います。
    print(chosen_preference)
    chosen_image = request.form["chosen_image"]
    print(chosen_image)

    # choice = input("どちらか選んでください")
    if chosen_preference == "食事" and chosen_image == "f_tukimi.jpg":
        photo = "f_chusonji.jpg"
        choice_1 = "景色がいいところで"
        choice_2 = "ちょっと一息"

        return render_template("index_2.html", choice_1=choice_1, choice_2=choice_2, photo=photo)

    elif chosen_preference == "写真" and chosen_image == "f_tukimi.jpg":
        photo = "f_tukimi.jpg"
        choice_1 = "お寺と"
        choice_2 = "風景と"

        return render_template("index_2.html", choice_1=choice_1, choice_2=choice_2, photo=photo)

    # elif chosen_preference == "食事" and chosen_image == "s_tukimi2.jpg":

    #     photo = "s_tukimi2.jpg"
    #     choice_1 = "景色がいいところで"
    #     choice_2 = "ちょっと一息"

    #     return render_template("index_2.html", choice_1=choice_1, choice_2=choice_2, photo=photo)

    # elif chosen_preference == "写真" and chosen_image == "s_tukimi2.jpg":

    #     photo = "s_tukimi2.jpg"
    #     choice_1 = "お寺と"
    #     choice_2 = "風景と"

    #     return render_template("index_2.html", choice_1=choice_1, choice_2=choice_2, photo=photo)

    elif chosen_preference == "食事" and chosen_image == "s_tukimi.jpg":
        photo = "s_tukimi.jpg"
        choice_1 = "景色がいいところで"
        choice_2 = "ちょっと一息"

        return render_template("index_2.html", choice_1=choice_1, choice_2=choice_2, photo=photo)

    elif chosen_preference == "写真" and chosen_image == "s_tukimi.jpg":
        photo = "s_tukimi.jpg"
        choice_1 = "お寺と"
        choice_2 = "風景と"
        return render_template("index_2.html", choice_1=choice_1, choice_2=choice_2, photo=photo)


@app.route("/index_3", methods=["POST"])
def select2():
    chosen_preference = request.form["chosen_preference"]
    # ここで chosen_preference を使って何か処理を行います。
    # choice = input("どちらか選んでください")
    print(chosen_preference)
    chosen_image = request.form["chosen_image"]
    print(chosen_image)

    if chosen_preference == "景色がいいところで" and chosen_image == "f_chusonji.jpg":
        photo = "s_tukimi.jpg"
        photo1 = "kannzann.jpg"
        photo2 = "yoshiie2.jpg"

        return render_template("index_3.html", photo=photo, photo1=photo1, photo2=photo2)

    elif chosen_preference == "ちょっと一息" and chosen_image == "f_chusonji.jpg":
        photo = "s_tukimi.jpg"
        photo1 = "bennkeienn.jpg"
        photo2 = "okunohosomiti2.jpg"
        return render_template("index_3.html", photo=photo, photo1=photo1, photo2=photo2)
    
    elif chosen_preference == "景色がいいところで" and chosen_image == "s_tukimi.jpg":
        photo = "s_tukimi.jpg"
        photo1 = "kannzann.jpg"
        photo2 = "yoshiie2.jpg"

        return render_template("index_3.html", photo=photo, photo1=photo1, photo2=photo2)

    elif chosen_preference == "ちょっと一息" and chosen_image == "s_tukimi.jpg":
        photo = "s_tukimi.jpg"
        photo1 = "bennkeienn.jpg"
        photo2 = "okunohosomiti2.jpg"
        return render_template("index_3.html", photo=photo, photo1=photo1, photo2=photo2)

    elif chosen_preference == "お寺と" and chosen_image == "f_tukimi.jpg":
        photo = "s_tukimi.jpg"
        photo1 = "konnjikidomae.jpg"
        photo2 = "bennzaitenn.jpg"

        return render_template("index_3.html", photo=photo, photo1=photo1, photo2=photo2)

    elif chosen_preference == "風景と" and chosen_image == "f_tukimi.jpg":
        photo = "s_tukimi.jpg"
        photo1 = "higasimonomi.jpg"
        photo2 = "tukimi.jpg"

        return render_template("index_3.html", photo=photo, photo1=photo1, photo2=photo2)
    
    elif chosen_preference == "お寺と" and chosen_image == "s_tukimi.jpg":
        photo = "s_tukimi.jpg"
        photo1 = "konnjikidomae.jpg"
        photo2 = "bennzaitenn.jpg"

        return render_template("index_3.html", photo=photo, photo1=photo1, photo2=photo2)

    elif chosen_preference == "風景と" and chosen_image == "s_tukimi.jpg":
        photo = "s_tukimi.jpg"
        photo1 = "higasimonomi.jpg"
        photo2 = "tukimi.jpg"

        return render_template("index_3.html", photo=photo, photo1=photo1, photo2=photo2)


@app.route("/index_4", methods=["POST"])
def select3():
    chosen_image = request.form["chosen_image"]
    if "sho" in chosen_image:
        photo = "s_tukimi2.jpg"

    else:
        photo = "f_chusonji.jpg"

    return render_template("index_4.html", photo=photo)


@app.route("/index_5", methods=["POST"])
def select4():
    chosen_preference = request.form["chosen_preference"]
    # ここで chosen_preference を使って何か処理を行います。
    print(chosen_preference)

    image = request.form["chosen_image"]
    if chosen_preference == "金鶏山":
        if "sho" in image:
            photo = "金鶏山１.jpg"
        else:
            photo = "金鶏山１.jpg"
    else:
        if "sho" in image:
            photo = "無量光院跡1.jpg"
        else:
            photo = "無量光院跡1.jpg"

    return render_template("index_5.html", photo=photo, image=image)


@app.route("/index_6", methods=["POST"])
def select5():
    chosen_preference = request.form["chosen_preference"]
    chosen_image = request.form["chosen_image"]
    if chosen_preference == "買い物＆休憩":
        if "sho" in chosen_image:
            photo1 = "あやめ.jpg"
            photo2 = "毛越寺松風庵.jpg"
        else:
            photo1 = "あやめ.jpg"
            photo2 = "毛越寺松風庵.jpg"
    else:
        if "sho" in chosen_image:
            photo1 = "毛越寺座禅.jpg"
            photo2 = "月見坂.jpg"
        else:
            photo1 = "毛越寺座禅.jpg"
            photo2 = "月見坂.jpg"

    return render_template("index_6.html", photo1=photo1, photo2=photo2)

    # @app.route("/index_6", methods=["POST"])
    # def select5():
    #     chosen_preference = request.form["chosen_preference"]
    #     # ここで chosen_preference を使って何か処理を行います。
    #     # choice = input("どちらか選んでください")
    #     chosen_image = request.form["chosen_image"]

    if chosen_preference == "買い物＆休憩":
        if "sho" in chosen_image:
            photo1 = "あやめ.jpg"
            photo2 = "毛越寺松風庵.jpg"
        else:
            photo1 = "あやめ.jpg"
            photo2 = "毛越寺松風庵.jpg"
    else:
        if "sho" in chosen_image:
            photo1 = "毛越寺座禅.jpg"
            photo2 = "月見坂.jpg"
        else:
            photo1 = "毛越寺座禅.jpg"
            photo2 = "月見坂.jpg"


#     return render_template("index_6.html", photo1=photo1, photo2=photo2)


@app.route("/index_7", methods=["POST"])
def select6():
    chosen_preference = request.form["chosen_preference"]
    # ここで chosen_preference を使って何か処理を行います。
    # choice = input("どちらか選んでください")
    chosen_image = request.form["chosen_image"]

    if chosen_preference == "sho":
        photo = "sho送り火.jpg"
    else:
        photo = "futa花火.jpg"

    return render_template("index_7.html", photo=photo)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
