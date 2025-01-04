import styles from "../styles/page.module.css";
import Header from "../components/header/header"
import Footer from "@/components/footer/footer";

export default function Home() {
  return (
    <div className={styles.page}>
      <Header/>
      <main className={styles.main}>
        <div>Calendar</div>
        <div>Filters</div>
      </main>
      <Footer/>
    </div>
  );
}

