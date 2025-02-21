import { useEffect, useRef, useState } from "react";

import { FaTag } from "react-icons/fa";
import { FaCalendarDays } from "react-icons/fa6";

import Item from "./components/Item";

import styles from "./App.module.css";

function App() {
  const [items, setItems] = useState<string[]>([
    "This is a sample item",
    "This is another sample item",
    "This is a third sample item",
    "This is a fourth sample item",
    "This is a fifth sample item",
  ]);
  const [tags, setTags] = useState<string[]>([
    "Tag 1",
    "Tag 2",
    "Tag 3",
    "Tag 4",
    "Tag 5",
    "Tag 6",
    "Tag 7",
    "Tag 8",
    "Tag 9",
    "Tag 10",
    "Tag 11",
    "Tag 12",
  ]);
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
    <main id={styles.main}>
      <div id={styles.app}>
        <ul id={styles.list}>
          {items.map((item, i) => (
            <Item
              key={item}
              id={i}
              content={item}
              onTick={() => removeItem(i)}
            />
          ))}
        </ul>
        <div id={styles.toolbar}>
          <ul id={styles.tags}>
            {tags.map((tag) => (
              <li key={tag}>{tag}</li>
            ))}
          </ul>
          <div id={styles.input}>
            <input
              ref={input}
              type="text"
              placeholder="Enter list item to add"
              onKeyDown={(e: React.KeyboardEvent<HTMLInputElement>) => {
                if (e.key === "Enter") {
                  addItem(e.currentTarget.value);
                  e.currentTarget.value = "";
                }
              }}
            />
            <button>
              <FaTag />
            </button>
            <button>
              <FaCalendarDays />
            </button>
          </div>
        </div>
      </div>
    </main>
  );
}

export default App;
