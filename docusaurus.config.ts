import { Config } from '@docusaurus/types';

const config: Config = {
  title: 'My Book',
  tagline: 'AI-native textbook',
  url: 'https://your-vercel-url.vercel.app',
  baseUrl: '/',
  favicon: 'favicon.ico',
  organizationName: 'muzammildha',
  projectName: 'my-book',
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: false,
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};

export default config;
