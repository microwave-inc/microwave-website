/*
THIS CODE BY LWJerri#3290
*/
const boxOwners = document.getElementById("owners_list");
/*
you can use this api but if you need to create custome api check:
 https://github.com/Hadi-Koubeissi/discord-web-api
*/
const API = "https://discord-api.microwavebot.tech/discord/user/";

const owners = [
    {
        "id": "398959101322854400",
        "post": "Founder & Head of Bot Development",
    },
    {
        "id": "597478415481700377",
        "post": "Co-Founder",
    },
    {
        "id": "384049625511755777",
        "post": "Bot and Website Developer",
    },
    {
        "id": "552104643446964225",
        "post": "Assistant Head of Bot Development",
    },
    {
        "id": "877750846400659527",
        "post": "Head of Website Development, Bot Developer",
    },
    {
        "id": "895321199675080704",
        "post": "Bot and Website Developer",
    },
]

for (let indexOne = 0; indexOne < owners.length; indexOne++) {
    const elementOwners = owners[indexOne];

    $.getJSON(API + elementOwners.id)
        .then(output => {
            if (!output.username || !output.url) {
                setTimeout(function () {
                    document.querySelectorAll(".banner img").forEach(imgs => imgs.src = url + "../assets/bot.png");
                }, 1000);
            }

            const ownerList = "<div id='trigger' class='card' style='margin: 15px;'><div class='banner'><img src='" + output.url + "'></div><br><h2 class='name' style='padding-top: 60px;'>" + output.username + "</h2><div class='title'><h1 id='trigger2' style='font-size: 26px; color: #000000;'>" + elementOwners.post + "</h2></div></div></div>"
            boxOwners.innerHTML += ownerList;
        });
}
