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
const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'introduction-to-physical-ai/index.mdx',
    'basics-of-humanoid-robotics/index.mdx',
    'module-01/index.mdx',
    'module-02/index.mdx',
    'module-03/index.mdx',
    'module-04/index.mdx',
    'capstone-ai-robot-pipeline/index.mdx',
  ],
};

export default sidebars;
