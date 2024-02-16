function clearResult() {
  
  document.getElementById("family-p").textContent = '';
  document.getElementById("scientific-name-p").textContent = '';
  document.getElementById("hausa-name-p").textContent = '';
  document.getElementById("common-p").textContent = '';
  document.getElementById("synonym-p").textContent = '';

  let noDataFoundTag = document.getElementById("no-data-found");
  if (noDataFoundTag) {
    noDataFoundTag.textContent = "";
  }

  let resItem = document.querySelectorAll(".res-item");
  resItem.forEach((item) => item.style.display = 'none');

  document.getElementById("result").style.display = 'none';

}


function fetchResults(searchBy, searchTerm) {
    const apiUrl = '/api/v1/plantinfo/';
    const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

    fetch(
        apiUrl,
        {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken
            },
            body: JSON.stringify({
                searchBy: searchBy,
                searchTerm: searchTerm,
            })
        }
    )
        .then(response => {
            console.log(response.status)
            console.log(response.status === 200)
            if (response.status === 200) {
                return response.json();
            } else {
                throw new Error("No data found");
            }
        })
        .then((data) => {
            document.getElementById("result").style.display = 'block';
            let resItem = document.querySelectorAll(".res-item")
            resItem.forEach((item) => item.style.display = 'flex')

            document.getElementById("family-p").textContent = data.family;
            document.getElementById("scientific-name-p").textContent = data.scientific_name;
            document.getElementById("hausa-name-p").textContent = data.hausa_name;
            document.getElementById("common-p").textContent = data.common_name;
            document.getElementById("synonym-p").textContent = data.synonym;
        })
        .catch((error) => {
            console.error('Error: ', error)
            document.getElementById("result").style.display = 'block';

            if (!document.getElementById("no-data-found")) {
                let noDataFoundDiv = document.createElement("div");
                noDataFoundDiv.className = "res-item";
    
                let noDataFoundTag = document.createElement("p");
                noDataFoundTag.id = 'no-data-found';
                noDataFoundTag.style.textAlign = 'center';

                noDataFoundTag.textContent = "No data found";

                noDataFoundDiv.appendChild(noDataFoundTag);
                document.getElementById("result").appendChild(noDataFoundTag);
            } else {
                const noDataFoundTag = document.getElementById("no-data-found");
                noDataFoundTag.textContent = "No data found";  
            }
        });
}

function fetchData() {
    clearResult();
    const searchBy = document.getElementById("search-by").value;
    const searchTerm = document.getElementById("search-input").value;
    if (searchTerm.length > 3) {
        fetchResults(searchBy, searchTerm);
    } else {
        document.getElementById("result").style.display = 'block';

        if (!document.getElementById("no-data-found")) {
            let noDataFoundDiv = document.createElement("div");
            noDataFoundDiv.className = "res-item";

            let noDataFoundTag = document.createElement("p");
            noDataFoundTag.id = 'no-data-found';
            noDataFoundTag.style.textAlign = 'center';
            noDataFoundTag.textContent = "No data found";

            noDataFoundDiv.appendChild(noDataFoundTag);
            document.getElementById("result").appendChild(noDataFoundTag);
        } else {
            const noDataFoundTag = document.getElementById("no-data-found");
            noDataFoundTag.textContent = "please enter a valid name";  
        }
    }

}
