import React from "react";

import styles from "./Input.module.css"; // Assuming you have a CSS module

const Input = React.forwardRef<
   HTMLInputElement,
   {
      addItem: (value: string) => void;
   }
>(({ addItem }, ref) => {
   return (
      <input
         id={styles.element}
         ref={ref}
         type="text"
         placeholder="Enter list item to add"
         onKeyDown={(e: React.KeyboardEvent<HTMLInputElement>) => {
            if (e.key === "Enter") {
               addItem(e.currentTarget.value);
               e.currentTarget.value = "";
            }
         }}
      />
   );
});

export default Input;
