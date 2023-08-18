import { useState } from "react";
import "./App.css";

type Restaurant = string;

function App() {
  const [input, setInput] = useState("");
  const [searchResults, setSearchResults] = useState<
    Record<Restaurant, string[][]>
  >({});

  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();

    fetch(`http://127.0.0.1:5000/search/all/${input}`)
      .then((res) => res.json())
      .then((data) => {
        setSearchResults(data);
      });

    setInput("");
  }

  function onInputChange(e: React.ChangeEvent<HTMLInputElement>) {
    setInput(e.target.value);
  }

  return (
    <>
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

      <div>
        {Object.keys(searchResults).map((k) => (
          <>
            <h2>{k}</h2>
            {searchResults[k].map((i) => (
              <p>{`${i[0]} $${i[1]}`}</p>
            ))}
          </>
        ))}
      </div>
    </>
  );
}

export default App;
