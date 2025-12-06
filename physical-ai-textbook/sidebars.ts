import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
 const sidebars = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Introduction',
      items: [
        'intro',
        'introduction-to-physical-ai',
      ],
    },
    {
      type: 'category',
      label: 'Basics',
      items: [
        'basics-of-humanoid-robotics',
      ],
    },
    {
      type: 'category',
      label: 'Modules',
      items: [
        'module-01/index',
        'module2/index',
        'module3/index',
        'module4/index',
      ],
    },
    {
      type: 'category',
      label: 'Capstone',
      items: [
        'capstone-ai-robot-pipeline',
      ],
    },
  ],
};

export default sidebars;

