import styles from "../styles/page.module.css";
import Menu from "../components/menu/menu";

export default function Home() {
  return (
    <div className={styles.pageContent}>
      <Menu />
      <div>column 2</div>
      <div>column 3</div>
    </div>
  );
}

