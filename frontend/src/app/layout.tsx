import type { Metadata } from "next";
import "../styles/globals.css";
import { Roboto } from 'next/font/google'
import styles from "../styles/page.module.css";
import Header from "../components/header/header";
import Footer from "@/components/footer/footer";

export const metadata: Metadata = {
  title: "To-do list",
  description: "App to keep track of my to-do list.",
};

const roboto = Roboto({
  weight: ['400', '700'],
  style: ['normal', 'italic'],
  subsets: ['latin'],
  display: 'swap',
})

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={roboto.className}>
      <body className={styles.gridContainer}>
        <Header />
        <main className={styles.main}>{children}</main>
        <Footer />
      </body>
    </html>
  );
}

