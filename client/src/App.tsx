import { useEffect, useRef, useState } from "react";

import Item from "./components/Item";
import Tags from "./components/Tags";
import Input from "./components/Input";

import styles from "./App.module.css";

type Item = {
   content: string;
   tags: string[];
   type:
   | "once"
   | "day"
   | "weekday"
   | "weekend"
   | "monday"
   | "tuesday"
   | "wednesday"
   | "thursday"
   | "friday"
   | "saturday"
   | "sunday"
   | "week"
   | "month";
};

function App() {
   const [items, setItems] = useState<Item[]>([]);
   const [tags, setTags] = useState<string[]>([]);
   const [selectedTags, setSelectedTags] = useState<string[]>([]);

   const input = useRef<HTMLInputElement>(null);

   const [waitingForResponse, setWaitingForResponse] = useState(false);
   const [itemsToAdd, setItemsToAdd] = useState<Item[]>([]);
   const [itemsToRemove, setItemsToRemove] = useState<Item[]>([]);
   const [loading, setLoading] = useState(true);

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
            setTags(data.tags);
            setLoading(false);
         });
   }, []);

   function addItem(content: string) {
      if (content === "") return;
      if (items.some((item) => item.content === content)) return;

      const newItem: Item = { content, tags: selectedTags, type: "once" };

      setItems([...items, newItem]);
      setItemsToAdd([...itemsToAdd, newItem]);
   }

   function removeItem(item: Item) {
      const newItems = items.slice();
      newItems.splice(newItems.indexOf(item), 1);
      setItems(newItems);
      setItemsToRemove([...itemsToRemove, item]);
   }

   if (loading) {
      return (
         <main id={styles.main}>
            <div id={styles.app}>
               <div>Loading...</div>
            </div>
         </main>
      );
   }

   return (
      <main id={styles.main}>
         <div id={styles.app}>
            <ul id={styles.list}>
               {items.map((item) => (
                  <>
                     {selectedTags.length === 0 ||
                        item.tags.some((tag) => selectedTags.includes(tag)) ? (
                        <Item
                           key={item.content}
                           content={item.content}
                           onTick={() => removeItem(item)}
                        />
                     ) : null}
                  </>
               ))}
            </ul>
            <div id={styles.toolbar}>
               <Tags
                  tags={tags}
                  selectedTags={selectedTags}
                  setSelectedTags={setSelectedTags}
               />
               <Input ref={input} addItem={addItem} />
            </div>
         </div>
      </main>
   );
}

export default App;
