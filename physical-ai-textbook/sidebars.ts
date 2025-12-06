import { SidebarConfig } from '@docusaurus/plugin-content-docs/src/sidebars/types.js';

const sidebars: SidebarConfig = {
  tutorialSidebar: [
    // Introduction section
    {
      type: 'category',
      label: 'Introduction',
      items: [
        'index',                       // main index                        // tutorial intro
        'introduction-to-physical-ai',  // intro to Physical AI
      ],
    },

    // Basics of Humanoid Robotics
    {
      type: 'doc',
      id: 'basics-of-humanoid-robotics',
    },
    // Modules
    {
      type: 'category',
      label: 'Chapter 2: Modules',
      items: [
        'module1/index',
        'module2/index',
        'module3/index',
        'module4/index',
      ],
    },

    // Capstone Pipeline
    {
      type: 'doc',
      id: 'capstone-ai-robot-pipeline',
    },

  ],
};

export default sidebars;
