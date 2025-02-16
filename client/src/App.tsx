import { useEffect, useRef, useState } from "react";

import "./App.css";

function App() {
   const [items, setItems] = useState([]);
   const input = useRef<HTMLInputElement>(null);

   useEffect(() => {
      fetch("/api/list")
         .then((response) => response.json())
         .then((data) => {
            console.log(data);
            setItems(data.items);
         });
   }, []);

   function addItem(newItem: string) {
      fetch("/api/list/add", {
         method: "POST",
         headers: {
            "Content-Type": "application/json",
         },
         body: JSON.stringify({ item: newItem }),
      }).then((response) => response.json());
   }

   return (
      <main>
         <h1>Items</h1>
         <ul>
            {items.map((item, i) => (
               <li key={i}>{item}</li>
            ))}
         </ul>
         <input ref={input} type="text" id="newItem" />
         <button
            onClick={() => {
               addItem(input.current!.value);
               input.current!.value = "";
            }}
         >
            Add
         </button>
      </main>
   );
}

export default App;
