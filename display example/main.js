
const dvMain = document.getElementById("dvMain");
const dvDetailsBG = document.getElementById("dvDetailsBG");
dvDetailsBG.addEventListener("click", () => {
    hideDetails();
});
const dvDetails = document.getElementById("dvDetails");
dvDetails.addEventListener("click", (e) => e.stopPropagation());

let data = [];

fetch("followingInfo.json").then((response) => {
    if (response.ok) response.text().then(createPageContent)
});

function createPageContent(text)
{
    data = JSON.parse(text);

    for (let i = 0; i < data.length; i++)
    {
        const p = document.createElement("a");
        p.innerHTML = data[i].displayname;
        p.dataset.id = i;
        p.onclick = (e) => {
            createUserDetails(e.target.dataset.id);
            e.preventDefault();
        };

        p.classList.add("item");

        dvMain.appendChild(p);
    }
}

function createUserDetails(id)
{
    dvDetails.replaceChildren();

    const hDisplayName = document.createElement("h3");
    const aHandle = document.createElement("a");
    const pDescription = document.createElement("p");
    const pLinksTitle = document.createElement("p");
    const ulLinks = document.createElement("ul");
    
    hDisplayName.innerHTML = data[id].displayname;
    aHandle.innerHTML = "@" + data[id].handle;
    aHandle.href = "https://twitter.com/" + data[id].handle;
    pDescription.innerHTML = data[id].description;
    pLinksTitle.innerHTML = "Links: ";

    for (let link of data[id].links)
    {
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.innerHTML = link;
        a.href = link;
        li.appendChild(a);
        ulLinks.appendChild(li);
    }

    dvDetails.appendChild(hDisplayName);
    dvDetails.appendChild(aHandle);
    dvDetails.appendChild(pDescription);
    dvDetails.appendChild(pLinksTitle);
    dvDetails.appendChild(ulLinks);

    showDetails();
}

function showDetails()
{
    dvDetailsBG.style.display = "block";
}

function hideDetails()
{
    dvDetailsBG.style.display = "none";
}

