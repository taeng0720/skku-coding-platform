// all routes here.
import {
  About,
  ACMRank,
  AnnouncementList,
  Announcement,
  ApplyResetPassword,
  EmailAuth,
  FAQ,
  Home,
  Logout,
  NotFound,
  OIRank,
  Problem,
  ProblemList,
  ResetPassword,
  SubmissionDetails,
  SubmissionList,
  UserHome
} from '../views'

import * as Contest from '@oj/views/contest'
import * as Setting from '@oj/views/setting'

export default [
  {
    name: 'home',
    path: '/',
    meta: { title: 'Home' },
    component: Home
  },
  {
    name: 'logout',
    path: '/logout',
    meta: { title: 'Logout' },
    component: Logout
  },
  {
    name: 'announcement-list',
    path: '/announcement',
    meta: { title: 'Announcement List' },
    component: AnnouncementList
  },
  {
    name: 'announcement-details',
    path: '/announcement/:announcementID',
    meta: { title: 'Announcement Detail' },
    component: Announcement
  },
  {
    name: 'apply-reset-password',
    path: '/apply-reset-password',
    meta: { title: 'Apply Reset Password' },
    component: ApplyResetPassword
  },
  {
    name: 'reset-password',
    path: '/reset-password/:token',
    meta: { title: 'Reset Password' },
    component: ResetPassword
  },
  {
    name: 'email-auth',
    path: '/email-auth/:token',
    meta: { title: 'Email Authentication' },
    component: EmailAuth
  },
  {
    name: 'problem-list',
    path: '/problem',
    meta: { title: 'Problem List' },
    component: ProblemList
  },
  {
    name: 'problem-details',
    path: '/problem/:problemID',
    meta: { title: 'Problem Details' },
    component: Problem
  },
  {
    name: 'submission-list',
    path: '/status',
    meta: { title: 'Submission List' },
    component: SubmissionList
  },
  {
    name: 'submission-details',
    path: '/status/:id/',
    meta: { title: 'Submission Details' },
    component: SubmissionDetails
  },
  {
    name: 'contest-list',
    path: '/contest',
    meta: { title: 'Contest List' },
    component: Contest.ContestList
  },
  {
    name: 'contest-problem-details',
    path: '/contest/:contestID/problem/:problemID/',
    component: Problem,
    meta: { title: 'Contest Problem Details' }
  },
  {
    name: 'contest-details',
    path: '/contest/:contestID/',
    component: Contest.ContestDetails,
    meta: { title: 'Contest Details' },
    children: [
      {
        name: 'contest-submission-list',
        path: 'submissions',
        component: SubmissionList
      },
      {
        name: 'contest-problem-list',
        path: 'problems',
        component: Contest.ContestProblemList
      },
      {
        name: 'contest-announcement-list',
        path: 'announcements',
        component: AnnouncementList
      },
      {
        name: 'contest-rank',
        path: 'rank',
        component: Contest.ContestRank
      },
      {
        name: 'acm-helper',
        path: 'helper',
        component: Contest.ACMContestHelper
      }
    ]
  },
  {
    name: 'acm-rank',
    path: '/acm-rank',
    meta: { title: 'ACM Rankings' },
    component: ACMRank
  },
  {
    name: 'oi-rank',
    path: '/oi-rank',
    meta: { title: 'OI Rankings' },
    component: OIRank
  },
  {
    name: 'user-home',
    path: '/user-home',
    component: UserHome,
    meta: { requiresAuth: true, title: 'User Home' }
  },
  {
    path: '/setting',
    component: Setting.Settings,
    children: [
      {
        name: 'default-setting',
        path: '',
        meta: { requiresAuth: true, title: 'Default Settings' },
        component: Setting.ProfileSetting
      },
      {
        name: 'profile-setting',
        path: 'profile',
        meta: { requiresAuth: true, title: 'Profile Settings' },
        component: Setting.ProfileSetting
      }
    ]
  },
  {
    path: '/about',
    name: 'about',
    meta: { title: 'About' },
    component: About
  },
  {
    path: '/faq',
    name: 'faq',
    meta: { title: 'FAQ' },
    component: FAQ
  },
  {
    path: '*',
    meta: { title: '404' },
    component: NotFound
  }
]