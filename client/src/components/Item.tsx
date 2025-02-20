import { useState } from "react";

import styles from "./Item.module.css";

function Item({
   id,
   content,
   onTick,
}: {
   id: number;
   content: string;
   onTick: () => void;
}) {
   const [isChecked, setIsChecked] = useState(false);

   return (
      <label id={styles.wrapper}>
         <input
            type="checkbox"
            onChange={() => {
               setIsChecked(!isChecked);

               setTimeout(() => {
                  onTick();
               }, 350);
            }}
         />
         <svg
            className={[
               styles.checkbox,
               isChecked ? styles.checkboxActive : "",
            ].join(" ")} // This element is purely decorative so
            // we hide it for screen readers
            aria-hidden="true"
            viewBox="0 0 15 11"
            fill="none"
         >
            <path
               d="M1 4.5L5 9L14 1"
               strokeWidth="var(--border-width)"
               stroke={isChecked ? "var(--color-background)" : "none"}
            />
         </svg>
         <span id={styles.content}>{content}</span>
      </label>
   );
}

export default Item;
