/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        files: {
          'light-gray': '#FBF9F9',
          'light-pink': '#FEE6E6',
          'super-light-red': '#F76E70',
          'bright-red': '#EE2B38',
          'primary-red': '#c11f32',
          'maroon': '#8E1021',
          'super-dark-maroon': '#4C151F',
          'headline-black': '#222222',
        }
      }
    },
  },
  plugins: [],
} 