import { Config } from '@docusaurus/types';

const config: Config = {
  title: 'My Book',
  tagline: 'AI-native textbook with RAG chatbot',
  url: 'https://your-vercel-domain.vercel.app', // replace with your Vercel URL
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'muzammildha',
  projectName: 'my-book',
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/muzammildha/my-book/edit/main/',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};

export default config;
