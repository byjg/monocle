{-# OPTIONS_GHC -fno-warn-missing-export-lists -fno-warn-unused-imports #-}

-- Generated by monocle-codegen. DO NOT EDIT!

-- |
-- Copyright: (c) 2021 Monocle authors
-- SPDX-License-Identifier: AGPL-3.0-only
module Monocle.Client.Api where

import Control.Monad.Catch (MonadThrow)
import Control.Monad.IO.Class (MonadIO)
import Monocle.Client (MonocleClient, monocleReq)
import Monocle.Config
import Monocle.Crawler
import Monocle.Search
import Monocle.UserGroup

configGetWorkspaces :: (MonadThrow m, MonadIO m) => MonocleClient -> GetWorkspacesRequest -> m GetWorkspacesResponse
configGetWorkspaces = monocleReq "api/2/get_workspaces"

configGetProjects :: (MonadThrow m, MonadIO m) => MonocleClient -> GetProjectsRequest -> m GetProjectsResponse
configGetProjects = monocleReq "api/2/get_projects"

configGetAbout :: (MonadThrow m, MonadIO m) => MonocleClient -> GetAboutRequest -> m GetAboutResponse
configGetAbout = monocleReq "api/2/about"

searchSuggestions :: (MonadThrow m, MonadIO m) => MonocleClient -> SuggestionsRequest -> m SuggestionsResponse
searchSuggestions = monocleReq "api/2/suggestions"

searchFields :: (MonadThrow m, MonadIO m) => MonocleClient -> FieldsRequest -> m FieldsResponse
searchFields = monocleReq "api/2/search/fields"

searchCheck :: (MonadThrow m, MonadIO m) => MonocleClient -> CheckRequest -> m CheckResponse
searchCheck = monocleReq "api/2/search/check"

searchQuery :: (MonadThrow m, MonadIO m) => MonocleClient -> QueryRequest -> m QueryResponse
searchQuery = monocleReq "api/2/search/query"

userGroupList :: (MonadThrow m, MonadIO m) => MonocleClient -> ListRequest -> m ListResponse
userGroupList = monocleReq "api/2/user_group/list"

userGroupGet :: (MonadThrow m, MonadIO m) => MonocleClient -> GetRequest -> m GetResponse
userGroupGet = monocleReq "api/2/user_group/get"

crawlerAddDoc :: (MonadThrow m, MonadIO m) => MonocleClient -> AddDocRequest -> m AddDocResponse
crawlerAddDoc = monocleReq "api/2/crawler/add"

crawlerCommit :: (MonadThrow m, MonadIO m) => MonocleClient -> CommitRequest -> m CommitResponse
crawlerCommit = monocleReq "api/2/crawler/commit"

crawlerCommitInfo :: (MonadThrow m, MonadIO m) => MonocleClient -> CommitInfoRequest -> m CommitInfoResponse
crawlerCommitInfo = monocleReq "api/2/crawler/get_commit_info"
