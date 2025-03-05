import styles from "./Input.module.css";

function Input({
  input,
  addItem,
}: {
  input: React.RefObject<HTMLInputElement>;
  addItem: (value: string) => void;
}) {
  return (
    <input
      id={styles.element}
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
  );
}

export default Input;
