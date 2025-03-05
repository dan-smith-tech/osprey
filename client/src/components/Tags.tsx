import styles from "./Tags.module.css";

function Tags({
  tags,
  selectedTags,
  setSelectedTags,
}: {
  tags: string[];
  selectedTags: string[];
  setSelectedTags: React.Dispatch<React.SetStateAction<string[]>>;
}) {
  return (
    <ul id={styles.tags}>
      {tags.map((tag) => (
        <>
          {selectedTags.includes(tag) ? (
            <li
              key={tag}
              className={selectedTags.includes(tag) ? styles.tagSelected : ""}
              style={{ "--color": "#2196F3" }}
              onClick={() => {
                if (!selectedTags.includes(tag))
                  setSelectedTags([...selectedTags, tag]);
                else setSelectedTags(selectedTags.filter((t) => t !== tag));
              }}
            >
              {tag}
            </li>
          ) : null}
        </>
      ))}
      {tags.map((tag) => (
        <>
          {!selectedTags.includes(tag) ? (
            <li
              key={tag}
              className={selectedTags.includes(tag) ? styles.tagSelected : ""}
              style={{ "--color": "#2196F3" }}
              onClick={() => {
                if (!selectedTags.includes(tag))
                  setSelectedTags([...selectedTags, tag]);
                else setSelectedTags(selectedTags.filter((t) => t !== tag));
              }}
            >
              {tag}
            </li>
          ) : null}
        </>
      ))}
    </ul>
  );
}

export default Tags;
