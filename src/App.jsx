import { useState } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Textarea } from '@/components/ui/textarea.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { CopyButton } from '@/components/ui/copy-button.jsx'
import { Modal } from '@/components/ui/modal.jsx'
import { MarkdownPreview } from '@/components/ui/markdown-preview.jsx'
import { Select } from '@/components/ui/select.jsx'
import { FileText, Wand2, Loader2, Sparkles, Eye, Trash2 } from 'lucide-react'
import './App.css'

function App() {
  const [rows, setRows] = useState([
    { 
      id: 1, 
      keyword: '', 
      product: 'Files.com', 
      contentLength: 'medium',
      articleTitle: '', 
      fullArticle: '', 
      metaTitle: '', 
      metaDescription: '', 
      status: 'empty',
      isLoading: false
    }
  ])
  const [previewModal, setPreviewModal] = useState({ isOpen: false, content: '', title: '' })

  const productOptions = [
    { value: 'Files.com', label: 'Files.com' },
    { value: 'ExaVault', label: 'ExaVault' },
    { value: 'ExpanDrive', label: 'ExpanDrive' },
    { value: 'Mover', label: 'Mover' }
  ]

  const contentLengthOptions = [
    { value: 'short', label: 'Short (500-800 words)' },
    { value: 'medium', label: 'Medium (800-1200 words)' },
    { value: 'long', label: 'Long (1200-2000 words)' },
    { value: 'comprehensive', label: 'Comprehensive (2000+ words)' }
  ]


  const removeRow = (id) => {
    if (rows.length > 1) {
      setRows(rows.filter(row => row.id !== id))
    }
  }

  const updateKeyword = (id, keyword) => {
    setRows(rows.map(row => 
      row.id === id ? { 
        ...row, 
        keyword, 
        status: keyword ? 'ready' : 'empty',
        // Clear content when keyword changes
        articleTitle: '',
        fullArticle: '',
        metaTitle: '',
        metaDescription: ''
      } : row
    ))
  }

  const updateProduct = (id, product) => {
    setRows(rows.map(row => 
      row.id === id ? { 
        ...row, 
        product,
        // Clear content when product changes
        articleTitle: '',
        fullArticle: '',
        metaTitle: '',
        metaDescription: '',
        status: row.keyword ? 'ready' : 'empty'
      } : row
    ))
  }

  const updateContentLength = (id, contentLength) => {
    setRows(rows.map(row => 
      row.id === id ? { 
        ...row, 
        contentLength,
        // Clear content when length changes
        articleTitle: '',
        fullArticle: '',
        metaTitle: '',
        metaDescription: '',
        status: row.keyword ? 'ready' : 'empty'
      } : row
    ))
  }

  const generateContent = async (id) => {
    const row = rows.find(r => r.id === id)
    if (!row.keyword) return

    setRows(rows.map(r => 
      r.id === id ? { ...r, isLoading: true } : r
    ))
    
    try {
      const response = await fetch('/api/generate_content', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          keyword: row.keyword,
          product: row.product,
          contentLength: row.contentLength
        })
      })
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      const data = await response.json()
      
      setRows(rows.map(r => 
        r.id === id ? { 
          ...r, 
          articleTitle: data.article_title,
          fullArticle: data.full_article,
          metaTitle: data.meta_title,
          metaDescription: data.meta_description,
          status: 'complete',
          isLoading: false
        } : r
      ))
    } catch (error) {
      console.error('Error generating content:', error)
      alert('Error generating content. Please make sure the backend server is running.')
      setRows(rows.map(r => 
        r.id === id ? { ...r, isLoading: false } : r
      ))
    }
  }

  const getStatusBadge = (status) => {
    const statusConfig = {
      'empty': { 
        label: 'Enter Keyword', 
        className: 'bg-files-light-gray text-files-headline-black border-files-light-pink px-3 py-1 rounded-full text-sm font-medium' 
      },
      'ready': { 
        label: 'Ready to Generate', 
        className: 'bg-files-light-pink text-files-primary-red border-files-super-light-red px-3 py-1 rounded-full text-sm font-medium' 
      },
      'complete': { 
        label: 'Complete', 
        className: 'bg-files-super-light-red/30 text-files-super-dark-maroon border-files-bright-red px-3 py-1 rounded-full text-sm font-medium' 
      }
    }
    
    const config = statusConfig[status] || statusConfig['empty']
    return (
      <div className={`inline-flex items-center gap-2 ${config.className}`}>
        <div className={`w-2 h-2 rounded-full ${
          status === 'empty' ? 'bg-files-headline-black/50' : 
          status === 'ready' ? 'bg-files-primary-red' : 
          'bg-files-bright-red'
        }`}></div>
        {config.label}
      </div>
    )
  }

  const openPreview = (content, title) => {
    setPreviewModal({ isOpen: true, content, title })
  }

  const closePreview = () => {
    setPreviewModal({ isOpen: false, content: '', title: '' })
  }

  const copyPreviewContent = () => {
    navigator.clipboard.writeText(previewModal.content)
      .then(() => {
        console.log('Article content copied to clipboard')
      })
      .catch(err => {
        console.error('Failed to copy content: ', err)
      })
  }


  return (
    <div className="min-h-screen bg-gradient-to-br from-files-light-gray via-files-light-pink to-files-super-light-red relative overflow-hidden">
      {/* Background decoration */}
      <div className="absolute inset-0 bg-[url('data:image/svg+xml,%3Csvg%20width%3D%2260%22%20height%3D%2260%22%20viewBox%3D%220%200%2060%2060%22%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%3E%3Cg%20fill%3D%22none%22%20fill-rule%3D%22evenodd%22%3E%3Cg%20fill%3D%22%239C92AC%22%20fill-opacity%3D%220.05%22%3E%3Ccircle%20cx%3D%2230%22%20cy%3D%2230%22%20r%3D%222%22/%3E%3C/g%3E%3C/g%3E%3C/svg%3E')] opacity-40"></div>
      
      <div className="relative z-10 p-4 lg:p-8">
        <div className="max-w-7xl mx-auto space-y-8">
          {/* Header */}
          <div className="text-center space-y-6">
            <div className="flex items-center justify-center gap-4 animate-fade-in">
              <div className="relative">
                <div className="absolute inset-0 bg-gradient-to-r from-files-primary-red to-files-bright-red rounded-2xl blur-lg opacity-30 animate-pulse"></div>
                <div className="relative p-4 bg-gradient-to-r from-files-primary-red to-files-bright-red rounded-2xl shadow-2xl transform hover:scale-105 transition-all duration-300">
                  <Sparkles className="h-10 w-10 text-white" />
                </div>
              </div>
              <div className="space-y-2">
                <h1 className="text-4xl lg:text-5xl font-bold bg-gradient-to-r from-files-primary-red via-files-bright-red to-files-maroon bg-clip-text text-transparent animate-gradient">
                  SEO Content Generator
                </h1>
                <div className="h-1 w-24 bg-gradient-to-r from-files-primary-red to-files-bright-red rounded-full mx-auto"></div>
              </div>
            </div>
            <div className="max-w-3xl mx-auto">
              <p className="text-lg lg:text-xl text-files-headline-black leading-relaxed font-medium">
                Generate complete SEO content in one click. Enter keywords and get full articles with titles, meta descriptions, and more.
              </p>
              <div className="mt-4 flex items-center justify-center gap-2 text-sm text-files-headline-black/70">
                <div className="w-2 h-2 bg-files-bright-red rounded-full animate-pulse"></div>
                <span>AI-Powered Content Generation</span>
              </div>
            </div>
          </div>


          {/* Content Cards */}
          <div className="grid gap-8">
            {rows.map((row, index) => (
              <Card key={row.id} className="group shadow-xl border-0 bg-white/90 backdrop-blur-sm rounded-2xl overflow-hidden hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-1">
                <CardHeader className="border-b border-files-light-pink bg-gradient-to-r from-files-light-gray to-files-light-pink relative overflow-hidden">
                  <div className="absolute inset-0 bg-gradient-to-r from-files-primary-red/5 to-files-bright-red/5"></div>
                  <div className="relative z-10 flex items-center justify-between">
                    <div className="flex items-center gap-4">
                      <div className="flex items-center gap-3">
                        <div className="p-2 bg-gradient-to-r from-files-primary-red to-files-bright-red rounded-lg shadow-md">
                          <FileText className="h-5 w-5 text-white" />
                        </div>
                        <div>
                          <CardTitle className="text-xl font-bold text-files-headline-black">
                            Content Row {index + 1}
                          </CardTitle>
                          <p className="text-sm text-files-headline-black/70">Generate SEO content for your keyword</p>
                        </div>
                      </div>
                      {getStatusBadge(row.status)}
                    </div>
                    {rows.length > 1 && (
                      <Button
                        onClick={() => removeRow(row.id)}
                        variant="ghost"
                        size="sm"
                        className="text-files-bright-red hover:text-files-maroon hover:bg-files-light-pink rounded-xl p-2 transition-all duration-200"
                      >
                        <Trash2 className="h-5 w-5" />
                      </Button>
                    )}
                  </div>
              </CardHeader>
              <CardContent className="p-8">
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                  {/* Input Section */}
                  <div className="space-y-6">
                    <div className="space-y-2">
                      <label className="block text-sm font-semibold text-files-headline-black mb-3">
                        Keyword *
                      </label>
                      <Input
                        placeholder="Enter your target keyword..."
                        value={row.keyword}
                        onChange={(e) => updateKeyword(row.id, e.target.value)}
                        className="w-full border-2 border-files-light-pink focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all duration-300 rounded-xl px-4 py-3 text-lg"
                      />
                    </div>
                    
                    <div className="space-y-2">
                      <label className="block text-sm font-semibold text-files-headline-black mb-3">
                        Product
                      </label>
                      <Select
                        value={row.product}
                        onChange={(value) => updateProduct(row.id, value)}
                        options={productOptions}
                        placeholder="Select product..."
                        className="w-full border-2 border-files-light-pink focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all duration-300 rounded-xl px-4 py-3 text-lg"
                      />
                    </div>

                    <div className="space-y-2">
                      <label className="block text-sm font-semibold text-files-headline-black mb-3">
                        Content Length
                      </label>
                      <Select
                        value={row.contentLength}
                        onChange={(value) => updateContentLength(row.id, value)}
                        options={contentLengthOptions}
                        placeholder="Select length..."
                        className="w-full border-2 border-files-light-pink focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all duration-300 rounded-xl px-4 py-3 text-lg"
                      />
                    </div>

                    <Button
                      onClick={() => generateContent(row.id)}
                      disabled={!row.keyword || row.isLoading}
                      className="w-full bg-gradient-to-r from-files-primary-red to-files-bright-red hover:from-files-maroon hover:to-files-primary-red text-white shadow-lg hover:shadow-xl transition-all duration-300 transform hover:scale-105 rounded-xl px-6 py-4 text-lg font-semibold disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
                    >
                      {row.isLoading ? (
                        <>
                          <Loader2 className="h-4 w-4 mr-2 animate-spin" />
                          Generating Content...
                        </>
                      ) : (
                        <>
                          <Wand2 className="h-4 w-4 mr-2" />
                          Generate Content
                        </>
                      )}
                    </Button>
                  </div>

                                     {/* Output Section */}
                  <div className="space-y-6">
                    <div className="space-y-2">
                      <label className="block text-sm font-semibold text-files-headline-black mb-3">
                        Article Title
                      </label>
                      <div className="relative">
                        <Textarea
                          placeholder="Article title will appear here..."
                          value={row.articleTitle}
                          readOnly
                          className="w-full h-24 resize-none text-base pr-12 border-2 border-files-light-pink bg-files-light-gray/50 rounded-xl px-4 py-3 focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all duration-300"
                        />
                        {row.articleTitle && (
                          <div className="absolute top-3 right-3">
                            <CopyButton text={row.articleTitle} />
                          </div>
                        )}
                      </div>
                    </div>

                     <div>
                       <label className="block text-sm font-semibold text-files-headline-black mb-3">
                         Meta Title
                       </label>
                       <div className="relative">
                         <Textarea
                           placeholder="Meta title will appear here..."
                           value={row.metaTitle}
                           readOnly
                           className="w-full h-20 resize-none text-base pr-12 border-2 border-files-light-pink bg-files-light-gray/50 rounded-xl px-4 py-3 focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all duration-300"
                         />
                         {row.metaTitle && (
                           <div className="absolute top-2 right-2">
                             <CopyButton text={row.metaTitle} />
                           </div>
                         )}
                       </div>
                     </div>

                     <div>
                       <label className="block text-sm font-semibold text-files-headline-black mb-3">
                         Meta Description
                       </label>
                       <div className="relative">
                         <div className="relative">
                           <Textarea
                             placeholder="Meta description will appear here..."
                             value={row.metaDescription}
                             readOnly
                             className="w-full h-24 resize-none text-base pr-12 border-2 border-files-light-pink bg-files-light-gray/50 rounded-xl px-4 py-3 focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all duration-300"
                           />
                           {row.metaDescription && (
                             <div className="absolute top-2 right-2">
                               <CopyButton text={row.metaDescription} />
                             </div>
                           )}
                         </div>
                       </div>
                     </div>
                   </div>
                </div>

                                 {/* Full Article Section */}
                 {row.fullArticle && (
                   <div className="mt-6 pt-6 border-t border-files-light-pink">
                     <div className="flex items-center justify-between mb-4">
                       <label className="block text-sm font-semibold text-files-headline-black">
                         Full Article
                       </label>
                       <div className="flex gap-2">
                         <button
                           onClick={() => openPreview(row.fullArticle, row.articleTitle)}
                           className="p-2 rounded-lg bg-files-light-pink hover:bg-files-super-light-red text-files-primary-red transition-all duration-200"
                           title="Preview Article"
                         >
                           <Eye className="h-5 w-5" />
                         </button>
                         <CopyButton text={row.fullArticle} />
                       </div>
                     </div>
                     <div className="relative">
                       <Textarea
                         placeholder="Full article will appear here..."
                         value={row.fullArticle}
                         readOnly
                         className="w-full h-48 resize-none text-base border-2 border-files-light-pink bg-files-light-gray/50 rounded-xl px-4 py-3 focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all duration-300"
                       />
                     </div>
                   </div>
                 )}
              </CardContent>
            </Card>
          ))}
        </div>
        </div>
      </div>

      {/* Article Preview Modal */}
      <Modal
        isOpen={previewModal.isOpen}
        onClose={closePreview}
        title={previewModal.title || 'Article Preview'}
        onCopy={copyPreviewContent}
      >
        <MarkdownPreview content={previewModal.content} />
      </Modal>
    </div>
  )
}

export default App 