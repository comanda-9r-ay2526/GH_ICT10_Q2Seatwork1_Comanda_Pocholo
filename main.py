from pyscript import document, display

kuni = ("China", "Japan", "Mongolia", "North Korea", "South Korea", "Taiwan", "Hong Kong", "Macau")
nick = ("The Red Dragon", "The Land of the Rising Sun", "Land of the Eternal Blue Sky", "The Hermit Kingdom", "Land of the Morning Calm", "Formosa", "Asia's World City", "Las Vegas of the East")

def show_nickname(e):
    damcountry = document.getElementById("kuni").value
    damnickname = nick[int(damcountry)]

    document.getElementById("thynick").innerText = "Nickname: " + damnickname