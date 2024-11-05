import { ReactNode, useState } from "react";
import "./App.css";

const ENV = import.meta.env;
const HOST = ENV.VITE_ENV == "prod" ? ENV.VITE_PROD_HOST : ENV.VITE_DEV_HOST;
const PROTOCOL = ENV.VITE_ENV == "prod" ? "https" : "http";

function App() {
  const [input, setInput] = useState("");
  const [searchResults, setSearchResults] = useState<string[][]>([]);

  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();

    // adjust endpoint based on environment
    fetch(`${PROTOCOL}://${HOST}/search/all/${input}`)
      .then((res) => res.json())
      .then((data) => {
        setSearchResults(data);
        // console.log(data);
      });

    setInput("");
  }

  function onInputChange(e: React.ChangeEvent<HTMLInputElement>) {
    setInput(e.target.value);
  }

  function formatResults(): ReactNode {
    let currentResaurant = "";

    // searchResult is an array of string arrays
    return searchResults.map((r, i) => {
      const name = r[0] || "";
      const price = r[1] || "";
      const restaurant = r[2] || "";

      // when we switch restaurants print the new restaurant header
      if (currentResaurant !== restaurant) {
        // update the currentRestaurant
        currentResaurant = restaurant;
        return (
          <div>
            <h2>{restaurant}</h2>
            <p>
              {name} {price}
            </p>
          </div>
        );
      }

      // print a regular item
      return (
        <p key={i}>
          {name} {price}
        </p>
      );
    });
  }

  return (
    <>
      {/* <h1>{test}</h1> */}
      <h1 className="title">What are you looking for?</h1>
      <form onSubmit={handleSubmit}>
        <input
          className="search-box"
          type="text"
          value={input}
          placeholder="Enter wine name or year"
          onChange={onInputChange}
        />
        <button type="submit">Submit</button>
      </form>
      <p>{searchResults.length} Results</p>

      <div>{formatResults()}</div>
    </>
  );
}

export default App;
