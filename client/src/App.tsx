import { useEffect, useRef, useState } from "react";

import "./App.css";

function App() {
   const [items, setItems] = useState<string[]>([]);
   const input = useRef<HTMLInputElement>(null);

   const [waitingForResponse, setWaitingForResponse] = useState(false);
   const [itemsToAdd, setItemsToAdd] = useState<string[]>([]);
   const [itemsToRemove, setItemsToRemove] = useState<number[]>([]);

   const timerRef = useRef(0);

   useEffect(() => {
      if (
         itemsToAdd.length > 0 ||
         (itemsToRemove.length > 0 && !waitingForResponse)
      ) {
         clearTimeout(timerRef.current);
         timerRef.current = setTimeout(() => {
            setWaitingForResponse(true);
            fetch("/api/list", {
               method: "POST",
               headers: {
                  "Content-Type": "application/json",
               },
               body: JSON.stringify({ itemsToAdd, itemsToRemove }),
            })
               .then((response) => {
                  setWaitingForResponse(false);

                  return response.json();
               })
               .catch((error) => {
                  setWaitingForResponse(false);

                  // TODO: Handle error
                  console.error(error);
               });
         }, 1000);
      }

      return () => clearTimeout(timerRef.current);
   }, [itemsToAdd, itemsToRemove, waitingForResponse]);

   useEffect(() => {
      fetch("/api/list")
         .then((response) => response.json())
         .then((data) => {
            setItems(data.items);
         });
   }, []);

   function addItem(newItem: string) {
      if (newItem === "") return;
      setItems([...items, newItem]);
      setItemsToAdd([...itemsToAdd, newItem]);
   }

   function removeItem(index: number) {
      const newItems = items.slice();
      newItems.splice(index, 1);
      setItems(newItems);
      setItemsToRemove([...itemsToRemove, index]);
   }

   return (
      <main>
         <h1>Items</h1>
         <ul>
            {items.map((item, i) => (
               <li key={i}>
                  {item}
                  <button
                     onClick={() => {
                        removeItem(i);
                     }}
                  >
                     Remove
                  </button>
               </li>
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
