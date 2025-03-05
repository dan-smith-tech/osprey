import styles from "./Input.module.css";

function Input({
  ref,
  addItem,
}: {
  input: React.RefObject<HTMLInputElement>;
  addItem: (value: string) => void;
}) {
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
}

export default Input;
