module.exports = {
  theme: {
    future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
    },
    purge: {
      layers: ["utilities"],
      content: [
        // Paths to your templates...
      ],
    },
    extend: {
      spacing: {
        "25vh": "25vh",
        "50vh": "50vh",
        "75vh": "75vh",
      },
      borderRadius: {
        xl: "1.5rem",
      },
    },
  },
  variants: {},
  plugins: [],
};
