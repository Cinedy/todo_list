import styles from "../styles/page.module.css";
import Menu from "../components/menu/menu";

export default function Home() {
  return (
    <div className={styles.pageContent}>
      <Menu />
    </div>
  );
}

